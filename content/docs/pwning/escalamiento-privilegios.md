---
title: "Escalamiento de Privilegios"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "pwning"
weight: 603
---

Teniendo acceso de usuario limitado a una máquina, y entendiendo mejor cómo funcionan los permisos y privilegios en Linux, podemos intentar ejecutar un _escalamiento de privilegios_, con el objetivo de conseguir acceso a un usuario con más permisos en la máquina. En el caso de un CTF, esto nos puede servir para acceder a archivos cuya lectura se encuentra limitada a ciertos usuarios. Estos archivos podrían contener pistas o incluso las flags que estamos buscando.

## Algunas convenciones de escalamiento de privilegios en CTFs

Hay algunas reglas implícitas en la ejecución de CTFs relacionadas con el escalamiento de privilegios, las cuales se enumeran a continuación:

- En general se busca conseguir acceso al usuario _root_, aunque también puede servir contar con acceso a un usuario con permisos de _sudo_ o a un usuario específico del sistema distinto al usuario con el que se inició el CTF.
- A veces no es necesario conseguir acceso directo a _root_, sino que basta con usar algún proceso que tiene ese acceso para exfiltrar información de esa cuenta.
- Luego de escalar privilegios con una cuenta, suele ser útil revisar su directorio `$HOME`:
  - En el caso de una cuenta _root_, este directorio se encuentra en `/root/`
  - En el caso de otra cuenta, el directorio suele encontrarse en `/home/<nombre_cuenta>`, donde `<nombre_cuenta>` corresponde al nombre de usuario de la cuenta con privilegios.
- En algunos casos, en el `$HOME` podría haber un archivo .txt (el cual podría estar oculto) con la flag, lo que finaliza el desafío. Sin embargo, si este archivo no existe, puede que necesitemos revisar si la flag está escondida de otra forma, o si podemos encontrar otra información interesante que nos permita avanzar en el desafío.

## Lista de estrategias genéricas para escalar privilegios

A continuación enumeramos algunas estrategias comunes para escalar privilegios en CTFs, varias de las cuales se encuentran enumeradas en [este apunte](https://d00mfist1.gitbooks.io/ctf/content/privilege_escalation_-_linux.html). Todas estas estrategias asumen que ya tienes un usuario con (al menos) permisos limitados en la máquina del CTF.

1. **¿Qué privilegios tengo por defecto?**: Tal vez la cuenta en la que estás logueado ya tiene permisos de superusuario. Para revisar esto, podemos ejecutar el comando `sudo -ll`. Este comando entregará información de si el usuario actual es o no un superusuario, o si tiene permisos para ejecutar algunos comandos con estos privilegios.

1. **¿Están bien colocados los permisos y _owners_ de carpetas sensibles?**: Vale la pena revisar si las carpetas sensibles del sistema poseen los permisos correctos. Por ejemplo, la carpeta `/root/` podría estar abierta a lectura o incluso escritura para todos los usuarios (`r o rw` en `other`). Esto se puede automatizar usando el comando `file` y la flag `-perm` seguida de `-ugo` (ojo con el guión al inicio), donde `u`, `g` y `o` son números en base octal que representan los permisos a buscar para el usuario (`u`), el grupo (`o`) o cualquiera (`o`). También están disponibles las flags `-group` y `-name` para filtrar por nombre y/o grupo del archivo o carpeta.

   - `find / -perm -007` buscaría desde la raíz del sistema de archivos todos los ficheros ejecutables por cualquier usuario.
   - `find / -name root` buscaría desde la raíz del sistema de archivos todos los ficheros cuyo dueño es el usuario `root`.
   - `find / -group root` buscaría desde la raíz del sistema de archivos todos los ficheros cuyo grupo es `root`.

1. **¿Están bien colocados los privilegios de `/etc/shadow/`?**: En el archivo `/etc/shadow` se guardan los hashes de las contraseñas de los usuarios del sistema. Si es legible, podemos intentar crackearlas con _John the Ripper_. Si es escribible, podemos cambiar un hash por uno elegido por nosotros:

   - `john --wordlist=<wordlist> hash` permite encontrar la palabra que genera cierto hash, donde `hash` es un archivo con el hash del archivo `/etc/shadow`.
   - `openssl passwd -1` crea un hash compatible con el archivo `/etc/shadow`.

1. **¿Hay programas con flag `setuid/setgid` habilitadas para un usuario con privilegios?**: Puede que exista un programa con flags `setuid/setgid` que reciba una entrada que sea explotable como para escalar privilegios o acceder a contenido restringido. Esto se puede revisar también con el comando `file` y la flag `-perm`, pero usando un número de 4 cifras (la primera siendo el valor de `setuid/setgid/sticky`):

   - `find / -perm -4000 ` buscaría desde la raíz del sistema de archivos todos los archivos con `setuid` encendido.

1. **¿Hay algún proceso corriendo con privilegios de forma periódica?**: En otros CTF existen programas que corren regularmente con un usuario con privilegios elevados, los cuales reciben de entrada algún archivo que es editable por un usuario con pocos privilegios. Modificar el archivo editable podría ayudar a cambiar el comportamiento del programa que corre automáticamente, facilitando la obtención de la `flag`. Es posible obtener estos procesos (y a veces la ruta del archivo ejecutable) con comandos especiales:

   - **Todos los procesos corriendo**: `ps aux` o `top`. En el caso de `top`, se muestra una tabla scrolleable con las flechas que muestra una lista de los procesos corriendo en la máquina.
   - **Procesos corriendo del usuario root**: `ps -u root`

1. **¿Hay algún archivo de configuración con contraseñas?**: Similar a lo que vimos en la unidad de forense, buscar archivos de configuración con usuarios/contraseñas en texto plano puede servir para escalar en privilegios, asumiendo que una de las contraseñas encontradas podría ser reutilizada como contraseña de un usuario con más permisos. Acá lo que podemos hacer es ejecutar algo como `grep -r password /` para buscar recursivamente en todos los archivos del sistema de archivos.

1. **¿Existe algún exploit específico para esta máquina?**: A veces la versión exacta del kernel de Linux o de algún programa corriendo en el sistema es propensa a algún exploit conocido. Para encontrar exploits asociados al sistema, podemos buscar sus aplicaciones y versiones con el comando `searchsploit` de Kali, o también buscar `exploit <programa> <version>` en nuestro buscador favorito para encontrar alguna prueba de concepto que nos permita escalar privilegios.
   - Para saber cuál es la versión del kernel de linux del sistema, ejecutar `uname -r`.

## Bypasses en programas especiales

A continuación mencionaremos algunos ejemplos de programas comunes que podrían estar asociados a `root` u otro usuario con privilegios y que podrían tener el byte `setuid` encendido, los cuales pueden ser usados para la ejecución arbitraria de código:

- **awk**: el comando `system("/bin/bash")` dentro de un bloque de `awk` permite ejecutar un programa de sistema, en este caso, una shell.
  - `awk 'BEGIN {system("/bin/bash")}'`
- **find**: la flag `exec` permite ejecutar un comando sobre cada archivo encontrado. El siguiente comando podría servir para levantar una shell:
  - `find --exec bash -i`.
- **vim**: Luego de iniciar `vim`, si presionas `escape`, escribes `:shell` y presionas `enter` podrás levantar una shell.
- **less**: `less` es un programa que sirve para ver archivos de texto extensos de forma paginada. Si se presiona la tecla `v` luego de abrir un archivo con `less`, se abrirá `vim` con los mismos permisos que `less`.
- **more**: Al igual que `less`, `more` permite leer archivos extensos. Si `more` abre un archivo cuya cantidad de líneas es mayor a la cantidad de líneas de la ventana de terminal, es posible levantar una shell escribiendo `!/bin/bash`.

Muchos otros ejemplos aparecen en [este apunte](https://d00mfist1.gitbooks.io/ctf/content/privilege_escalation_-_linux.html), en la sección _Abusing sudo-rights_. Además, [este sitio](https://gtfobins.github.io/) agrupa una lista colaborativa de cientos de binarios con estas características.

La recomendación general es que al encontrar algún otro programa con `setuid` y `owner root`, investiguen si existe una forma de ejecutar código arbitrario. Si el programa es conocido, busquen en su documentación o sitios de referencia y ayuda. Si el programa es un script propio de la máquina, revisen su código fuente para ver cómo abusar de sus funcionalidades para ejecutar código arbitrario.

## Scripts de enumeración automática

Existen muchas herramientas de código abierto que automatizan algunas de las recomendaciones entregadas en el paso anterior, además de ejecutar otras técnicas más avanzadas para intentar escalar privilegios en una máquina de CTF. A continuación enumeramos algunos de estos programas:

- [Linux Exploit Suggester](https://github.com/mzet-/linux-exploit-suggester)
- [LinEnum](https://github.com/rebootuser/LinEnum)
- [Unix-Privesc-Check](http://pentestmonkey.net/tools/audit/unix-privesc-check)
- [LinPrivchecker.py](https://github.com/reider-roque/linpostexp/blob/master/linprivchecker.py)

Les recomendamos revisar también [este enlace](https://github.com/Ignitetechnologies/Privilege-Escalation) para encontrar harto material de escalamiento de privilegios.

### Reverse Shell

En algunas ocasiones, si bien no podemos escalar privilegios directamente en el sistema, sí podemos hacer que el usuario root ejecute (a través de un trabajo periódico o de otra forma) un comando a nuestra elección. En estos casos, nos conviene levantar una `reverse shell`, es decir, hacer que el usuario root abra una sesión de shell y la deje disponible para que nos conectemos a ella vía `nc`. Pueden ver la sección dedicada a `reverse shells` en la unidad de Aplicaciones Web para encontrar una explicación más detallada de esta técnica.
