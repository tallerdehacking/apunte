---
title : "Comandos, Logs y Configuraciones"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "forense"
weight: 402

---

En esta página veremos algunos comandos útiles para problemas de forense y enumeraremos algunas rutas comunes en las que se suelen almacenar logs y archivos de configuración de programas y servicios de común uso.

## Comandos útiles para análisis forense

Estos comandos pueden ser útiles tanto en forensics como en otras preguntas de CTF. También les pueden servir en la vida, si trabajan con terminales de Linux.

* `find`: Permite encontrar un archivo por su nombre, tipo, tamaño, etc.
  * **Encontrar un archivo por nombre (_case insensitive_) en una carpeta o sus subcarpetas**: `find -iname nombre`
  * **Encontrar todos los archivos de extensión `md` en una carpeta o sus subcarpetas**: `find -regex ".*\.md"`
  * **Encontrar todos los archivos no vacíos en una carpeta o sus subcarpetas**: `find -not -empty`
* `grep`: Permite encontrar un archivo por su contenido. Soporta expresiones regulares
  * **Buscar una palabra en un archivo**:
  * **Buscar una palabra en una carpeta y sus subcarpetas**:
  * **Buscar una [expresión regular](https://regexr.com)**: 
* `awk`: Pequeño pero potente lenguaje de programación que permite realizar operaciones sobre archivos de texto semi estructurados. Les recomiendo [este tutorial](http://www.hcs.harvard.edu/~dholland/computers/awk.html) para aprender a utilizarlo.
  * **Mostrar solo la tercera columna de un archivo CSV**: `awk -F"," '{print $2} < archivo.csv'`
* `sed`: Utilidad que facilita el reemplazar caracteres por otros en un archivo de texto.
  * **Reemplazar en todo un archivo los números por `x`**: `echo "1-hola 2-adios 9213-chao" | sed "s/[0-9]/x/g"`
* `tr`: Utilidad que facilita el _transponer_ (desplazarlos) o eliminar caracteres de un archivo de texto.
  * **Cifrar o descifrar un mensaje en ROT13**: `echo "hola" | tr a-z n-za-m`
  * **Eliminar tildes de una cadena de texto**: `echo "ácido gélido sísmico lógico único" | tr -d áéíóú`
  * **Reemplazar tildes de una cadena de texto por las vocales respectivas**: `echo "ácido épico sísmico lógico único" | tr áéíóú aeiou`
* `sort`: Comando útil para ordenar las líneas de un archivo alfabéticamente.
  * **Ordenar un archivo spearado por tabs según su segunda columna en orden reverso (parámetro numérico)**: `sort --key 2 --reverse --numeric-sort archivo.tsv`
* `uniq`: Programa que permite eliminar o aislar repetidos en archivo ordenado alfabéticamente.
  * **Eliminar líneas repetidas**: `uniq archivo.txt`
  * **Dejar líneas repetidas**: `uniq -d archivo.txt`


Para entender mejor como usar cada utilidad, les recomendamos ejecutar `man <nombre_comando>` en sus computadores.

## Logs

Un archivo de `log` registra información importante relacionada a la ejecución de un proceso o sistema operativo.

Los archivos de log son interesantes en CTFs debido a que, dependiendo del nivel de verbosidad con el que estén configurados, podrían quedar guardados datos sensibles en ellos. (como IPs, contenido de consultas o incluso contraseñas).

A continuación haremos una lista breve de algunos logs importantes en sistemas operativos basados en Linux y servicios que suelen correrse sobre ellos.

### Logs de sistema

* [`journalctl`](https://man7.org/linux/man-pages/man1/journalctl.1.html): Herramienta que permite revisar logs del `journal` de los sistemas operativos basados en Linux con Systemd. Al ejecutarla sin argumentos, es posible ver los `logs` del sistema relacionados con el kernel, el booteo y los servicios administrados por `systemd` desde el más antiguo guardado.
  * Al usar la flag `-r` los logs se muestran en orden reverso (parte con los más recientes)
  * La flag `-f` permite mantener en observación los logs, mostrando los nuevos mensajes apenas se emiten.
  * Es posible ver otras flags en el link de esta sección.

* `syslog`: Algunos servicios guardan sus logs en un archivo denominado `syslog`:
  * En Ubuntu este archivo está en `/var/log/syslog`
  * En OSes basados en CentOS, se guarda en `/var/log/messages`

### Logs de aplicaciones

La carpeta `/var/log/` suele contener logs de los servicios instalados en un sistema operativo basado en Linux. Algunas aplicaciones interesantes para revisar sus logs:

* **Servidores Web**: Servicios que se encargan de contestar las consultas realizadas por un navegador web (o cualquier programa que "hable" HTTP/HTTPS). Generalmente escuchan en los puertos 80 y 443. Algunos servidores web comunes:
  * **Apache**: Este servidor guarda dos tipos de logs:
    * **Logs de Acceso**: Se almacenan las IP de los clientes y las rutas accedidas por ellos. Puede estar guardado en alguna de las siguientes rutas, aunque podría variar entre distribuciones y configuraciones:
      * `/var/log/httpd/access_log`
      * `/var/log/apache2/access.log`
      * `/var/log/httpd-access.log`
    * **Logs de Error**: Suelen ser específicos para cada _virtual host_ del servidor.  La mejor forma de hallar su ubicación es revisando el archivo de configuración de Apache el string `ErrorLog`. (¿Cómo encontrarían el archivo de configuración de apache si solo saben que está en la carpeta `/etc/`?)
  * **NGINX**: Al igual que Apache, separa sus logs según tipo. La siguiente es una ubicación posible, pero les recomendamos :
    * **Logs de Acceso**: `/var/log/nginx/access.log`
    * **Logs de Error**: `/var/log/nginx/error_log`
* **Servidor SSH e inicio de sesión**: El acto de iniciar sesión exitosa o fallidamente suele quedar registrado en el sistema. A continuación se detallan los comandos necesarios para revisar estos registros.
  * **Logs de inicio de sesión exitosos** `last`
  * **Inicios de sesión fallidos** `last -b /var/log/btmp`

## Archivos de configuración

Los archivos de configuración de las aplicaciones de Linux suelen estar en la carpeta `/etc/`.
  * **Apache**: `/etc/apache2`
  * **NGINX**: `/etc/nginx`
  * **SSH Daemon**: `/etc/ssh`
A continuación mencionamos algunos archivos de configuración de sistema interesantes:

* **Usuarios**: El archivo `/etc/passwd` posee una lista de todos los usuarios del sistema.
* **Grupos**: El archivo `/etc/group` posee una lista de todos los grupos de usuario del sistema.
* **Sudoers**: El archivo `/etc/sudoers` y los archivos en `/etc/sudoers.d/` definen los usuarios con permisos para utilizar el comando `sudo`, que permite ejecutar acciones como superusuario. 


