---
title : "Permisos en Linux"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "anexos"
weight: 048
---

Esta sección explica de forma breve el sistema de permisos en sistemas de archivo utilizados comúnmente en sistemas operativos Linux.

## Usuarios y Grupos

En estos sistemas operativos, cada usuario tiene un ID definido en el archivo `/etc/passwd`. En algunas distribuciones de Linux, este ID crece de forma incremental, mientras que en otras se reservan los UID inferiores a 1000 para "metausuarios" (usuarios usados por procesos de Linux) y los superiores para usuarios normales.

El SO también permite contar con "grupos", los cuales están definidos en el archivo `/etc/group`  y también tienen un ID característico. Un usuario puede estar en 0 o más grupos sin problemas. Algunos sistemas crean a cada usuario un grupo con el mismo ID (pero en el archivo `/etc/group`) y agregan al usuario a ese grupo.

Los grupos suelen servir para definir permisos tanto en archivos como en ejecución de comandos (como cuando se agrega un usuario al grupo `wheel` para tener permisos de superusuario). Más adelante explicaremos como se hace esto.

## Owners y Groups

En sistemas de archivo compatibles con Linux, cada archivo creado tiene las siguientes propiedades:

* Un `owner` o dueño del archivo
* Un `group` o grupo con permisos en el archivo
* Un set de `permisos de archivo`.

### Agregar-Remover de un grupo a un usuario

* **Agregar Usuario a grupo** `gpasswd -a USER GROUP`
* **Eliminar Usuario a grupo** `gpasswd -d USER GROUP`

## Permisos en Archivos y Carpetas

Cada archivo o carpeta posee 9 bits para definir permisos:

* 3 bit están asociados al `owner` del archivo
* 3 bit están asociados a personas del `group` del archivo
* 3 bit están asociados a todos los demás usuarios (`other`) (o sea, que no cumplan alguna de las otras dos condiciones).

```
| R W X | R W X | R W X |
| x x x | x x x | x x x |
| Owner | Group | Other |
```

Las acciones de permisos son las siguientes:

* **Read** (R) Permite leer el archivo o acceder a la carpeta.
* **Write** (W) Permite editar el archivo o crear nuevos archivos en la carpeta.
* **Execute** (X) Permite ejecutar el archivo o listar los archivos internos de la carpeta.

Los permisos suelen ser representados como números en octal:

```
| R W X | R W X | R W X |
| 1 0 0 | 1 1 1 | 0 0 0 |
| Owner | Group | Other |
```

Lo anterior corresponde al número `470`.

Si el bit está marcado con un 1, significa que el usuario puede ejecutar esa acción.

## Comandos para cambiar permisos

* `chown`: Permite cambiar el `owner` (y group si se adjunta el GID después del UID y `:`) de un archivo/carpeta. Necesitas hacerlo como `root` o con `sudo`. La flag `-R` ejecuta la operación de forma recursiva.
  * `chown 1234:1234 file` cambia el `UID` de `file` a `1234` y el `GID` de `file` a `1234`.
* `chgrp`: Permite cambiar el `group` de un archivo/carpeta. Necesitas hacerlo como `root` o con `sudo`. La flag `-R` ejecuta la operación de forma recursiva.
  * `chgrp 1234 file` cambia el `GID` de `file` a `1234` y deja su `UID` como antes.
* `chmod`: Permite cambiar los permisos de un archivo/carpeta.
  * `chgrp 740 file` cambia los permisos del archivo `file` a `RWX` para su `owner`, `R` para su `group` y nada para `other`.
* `umask`: Define los permisos por defecto al crear archivos en una sesión de terminal. Los permisos por defecto son el inverso del valor configurado con `umask`.
  * `chgrp 022` setea como permiso por defecto `644` al crear un nuevo archivo. 
* `ls -ln` permite ver los archivos de una carpeta y sus permisos en formato numérico. Si sacas el argumento `n` se ve el nombre del usuario o grupo.