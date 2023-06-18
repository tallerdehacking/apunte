---
title: "Permisos de Usuario en Linux"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "pwning"
weight: 602
---

## Permisos de Usuario en Linux

Esta sección explica de forma breve el sistema de permisos en sistemas de archivo utilizados comúnmente en sistemas operativos Linux.

### Usuarios y Grupos

En estos sistemas operativos, cada usuario tiene un ID definido en el archivo `/etc/passwd`. En algunas distribuciones de Linux, este ID crece de forma incremental, mientras que en otras se reservan los UID inferiores a 1000 para "metausuarios" (usuarios usados por procesos de Linux) y los superiores para usuarios normales.

El SO también permite contar con "grupos", los cuales están definidos en el archivo `/etc/group` y también tienen un ID característico. Un usuario puede estar en 0 o más grupos sin problemas. Algunos sistemas crean a cada usuario un grupo con el mismo ID (pero en el archivo `/etc/group`) y agregan al usuario a ese grupo.

Los grupos suelen servir para definir permisos tanto en archivos como en ejecución de comandos (como cuando se agrega un usuario al grupo `wheel` para tener permisos de superusuario). Más adelante explicaremos como se hace esto.

### Owners y Groups de archivos

En sistemas de archivo compatibles con Linux, cada archivo creado tiene las siguientes propiedades:

- Un `owner` o dueño del archivo
- Un `group` o grupo con permisos en el archivo
- Un set de `permisos de archivo`.

#### Agregar-Remover de un grupo a un usuario

- **Agregar Usuario a grupo** `gpasswd -a USER GROUP`
- **Eliminar Usuario a grupo** `gpasswd -d USER GROUP`

### Permisos en Archivos y Carpetas

Cada archivo o carpeta posee 9 bits para definir permisos:

- 3 bit están asociados al `owner` del archivo
- 3 bit están asociados a personas del `group` del archivo
- 3 bit están asociados a todos los demás usuarios (`other`) (o sea, que no cumplan alguna de las otras dos condiciones).

```
| r w x | r w x | r w x |
| x x x | x x x | x x x |
| Owner | Group | Other |
```

Las acciones de permisos son las siguientes:

- **Read** (R) Permite leer el archivo o acceder a la carpeta.
- **Write** (W) Permite editar el archivo o crear nuevos archivos en la carpeta.
- **Execute** (X) Permite ejecutar el archivo o listar los archivos internos de la carpeta.

Los permisos suelen ser representados como números en octal:

```
| r w x | r w x | r w x |
| 1 0 0 | 1 1 1 | 0 0 0 |
| Owner | Group | Other |
```

Lo anterior corresponde al número `470`.

Si el bit está marcado con un 1, significa que el usuario puede ejecutar esa acción.

### Comandos para cambiar permisos

- `chown`: Permite cambiar el `owner` (y group si se adjunta el GID después del UID y `:`) de un archivo/carpeta. Necesitas hacerlo como `root` o con `sudo`. La flag `-R` ejecuta la operación de forma recursiva.
  - `chown 1234:1234 file` cambia el `UID` de `file` a `1234` y el `GID` de `file` a `1234`.
- `chgrp`: Permite cambiar el `group` de un archivo/carpeta. Necesitas hacerlo como `root` o con `sudo`. La flag `-R` ejecuta la operación de forma recursiva.
  - `chgrp 1234 file` cambia el `GID` de `file` a `1234` y deja su `UID` como antes.
- `chmod`: Permite cambiar los permisos de un archivo/carpeta.
  - `chgrp 740 file` cambia los permisos del archivo `file` a `RWX` para su `owner`, `R` para su `group` y nada para `other`.
- `umask`: Define los permisos por defecto al crear archivos en una sesión de terminal. Los permisos por defecto son el inverso del valor configurado con `umask`.
  - `chgrp 022` setea como permiso por defecto `644` al crear un nuevo archivo.
- `ls -ln` permite ver los archivos de una carpeta y sus permisos en formato numérico. Si sacas el argumento `n` se ve el nombre del usuario o grupo.

### Superusuarios

En sistemas basados en Unix, existe un usuario con privilegios totales, denominado superusuario. En general es llamado `root` y posee como `user id` el número 0. De hecho, si cambias el `user id` de cualquier usuario a 0 en `/etc/passwd`, éste se comportara como si fuera el usuario `root`. Sin embargo, esto solo transformaría al otro usuario en `root` y no permitiría crear dos usuarios separados que tengan permisos de superusuario.

Para resolver este problema, existe un comando llamado `sudo`, el cual permtie ejecutar otros comandos que requieran privilegios de superusuario si y solo sí se está incluído en un archivo especial: `/etc/sudoers`. Varios sistemas operativos tienen configurado este archivo por defecto para que los usuarios incluidos en el grupo `sudo` o `wheel` puedan ejecutar comandos de superusuario, pero nada evita que uno pueda editar `/etc/sudoers` para cambiar este comportamiento.

#### Archivo `/etc/sudoers`

El archivo `/etc/sudoers` tiene una sintaxis especial para permitir a un usuario, a un grupo de usuarios o a todos los usuarios ejecutar uno o más comandos con permisos de superusuario. A continuación unos ejemplos de configuración, pero es posible leer más sobre ella en [este artículo](https://toroid.org/sudoers-syntax):

```bash
%wheel ALL=(ALL) NOPASSWD: ALL
```

Lo anterior quiere decir que todos los usuarios del grupo Wheel pueden ejecutar cualquier comando como cualquier usuario sin necesidad de solicitarles la contraseña.

Por otro lado, si se quieren asignar permisos solamente a un usuario, la sintaxis es así:

```bash
User Host = (Runas) Command
```

Esto quiere decr que el usuario `User` puede ejecutar el comando `Command` como el usuario `Runas` en el host `Host`. Si cualquiera de estos parámetros es `ALL`, calza con cualquier usuario/host/comando. El valor `Command` incluso puede ser el prefijo de un comando con argumentos incluidos. Y cuando calce con el comando ejecutado, se permitirá su utilización como otro usuario con `sudo`. **Ojo que el prefijo debe ser exacto**, es decir, si `command` incluye la ruta absoluta del comando a ejecutar con sudo, siempre será necesario declarar esa ruta absoluta.

### `setuid`, `setgid` y `sticky bit`

Existen bits de permisos especiales en sistemas operativos basados en Unix, los cuales permiten la ejecución de un programa como si se fuera el usuario owner del archivo o se estuviera en el group del archivo. Estos se llaman `setuid` y `setgid` (para usuarios y grupos, respectivamente). Algunos comandos necesitan tener estos bits seteados para que puedan ser usados por cualquier otro usuario en el sistema.

También existe el `sticky bit`, el cual en Linux permite configurar un directorio para que solamente su propietario pueda renombrar o eliminar archivos en él.

Su orden es el siguiente

```
| setuid | setgid | sticky |
```

Para activar estos bits es necesario declarar un número octal extra al usar chmod. Por ejemplo, `chmod 6755` cambia los permisos del archivo a `755`, pero al mismo tiempo setea los bit `setuid`, `setgid` y `sticky`. Estos bit se verán de la siguiente forma al hacer `ls`:

```bash
[eriveros@arcozen cc5325]$ ls -alh
total 0
drwxr-xr-x  2 eriveros eriveros  60 May 31 01:44 .
drwxrwxrwt 24 root     root     720 May 31 01:44 ..
-rwsr-sr-t  1 eriveros eriveros   0 May 31 01:44 file
```

Por si no se nota, los bits `x` de `user` y `group` cambian a `s` (o `S` si la flag `x` del usuario o grupo no están seteadas) para indicar que se cuenta con los bits `setuid` y `setgid` fijados. En el caso del sticky bit, este se verá como una `t` en el bit de ejecución `other` del archivo (o una `T` si es que other no tiene permiso de ejecución).

- **En archivos**:
  - `setuid`: Activar este bit sirve para que el usuario ejecute el programa como si fuera el usuario dueño del programa.
  - `setgid`: Activar este bit sirve para que el usuario ejecute el programa como si estuviese dentro del grupo dueño del programa.
  - `sticky bit`: No se utiliza en archivos en Linux (no tiene efecto)
- **En carpetas**:
  - `setuid`: causa que los archivos y carpetas creados dentro de ella obtengan por defecto como `owner` al owner de la carpeta en la cual se setearon los bytes.
  - `setgid`: causa que los archivos y carpetas creados dentro de ella obtengan como grupo por defecto al grupo al que pertenece la carpeta en la cual se setearon los bytes.
  - `sticky bit`: evita que las personas que no sean dueñas de una carpeta puedan crear o borrar archivos en ella.

### Archivos Ocultos

Si bien esto no tiene que ver específicamente con permisos, es útil saber qué es un archivo oculto en Linux.

Un archivo oculto corresponde a un archivo que no se ve directamente al hacer `ls` de una carpeta. Estos archivos son todos los que su nombre parte con un punto `.`. Por ejemplo, en los directorios `$HOME` algunos programas guardan archivos de configuración o de estado especiales, cuyos nombres parten con punto. `.bash_history` (historial de comandos de bash), `.bashrc` (script que se ejecuta al iniciar una nueva sesión de bash), `.config` suelen ser carpetas y archivos ocultos que aparecen en los `$HOME` de usuarios debido a que otros programas los crean.

Para ver estos archivos, es necesario pasar la flag `-a` al comando `ls`. Esta flag se puede combinar con otras flags ya vistas (como `l` y `n`).
