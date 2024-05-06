---
title : "Versionado y Recuperación de Archivos"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "forense"
weight: 403

---

Esta página tratará de dos enfoques distintos para recuperar información. El primero corresponde al uso de sistemas de control de versiones, mientras que el segundo desc

## Sistemas de Control de Versión

Al desarrollar aplicaciones, se suelen utilizar **sistemas de control de versión**, tanto para administrar las colaboraciones de múltiples personas o equipos, como para llevar un historial en el tiempo de los cambios realizados en el código. Esto último es bastante beneficioso en casos en los que es necesario revertir algún cambio, pero puede llevar a la persistencia de la difusión accidental de valores confidenciales.

A modo de ejemplo, en el curso veremos herramientas para revisar el sistema de control de versión _git_. Sin embargo, muchas de estas técnicas podrían aplicar de igual manera en otros sistemas, como _Mercurial_, _SVN_, _Pijul_, etc.\

### Git

[Git](https://git-scm.com/) es un sistema de control de archivos distribuido creado por Linus Torvalds el año 2005, para utilizarlo en el desarrollo del Kernel de Linux en reemplazo a una herramienta llamada `BitKeeper`. Hoy es una de las herramientas más populares para el control de versiones de código.

#### Funcionamiento de Git

Git almacena información del versionamiento en dos estructuras distintas:

* Un **índice mutable** que almacena el estado actual del versionamiento.
* Un _storage_ de **objetos inmutables** que guarda todas las versiones almacenadas de los archivos del repositorio.

Además, define los siguientes conceptos para manejar el versionamiento:

* `Blob` representa una versión completa de un archivo, guardada en el _storage_ inmutable. 
* `Commit` es un conjunto de blobs y representa un estado en el repositorio, identificado por un _hash SHA-1_. Un commit puede tener uno o más _padres_. 
* `Branch` o `rama` es un puntero a un conjunto de _commits_ representado por el último commit de la rama. A medida se agregan commits en una rama, el puntero se va moviendo de forma automática. Lo anterior genera una estructura similar a un `árbol`.
* `Remote` representa una versión del mismo repositorio en una máquina remota. Es posible enviar los cambios locales a esa versión (`push`) o traerse cambios remotos de esa versión (`pull`).
* `Staging` es donde se almacenan los archivos que desean ser agregados al próximo commit.
* `master` o `main` es el nombre del puntero al último commit de la rama principal.
* `tag` es una referencia fija a algún commit en especial. Son útiles para marcar en el arbol
* `HEAD` es un puntero al último commit de la rama actual.

#### Comandos útiles en Git

* **Inicializar Repositorio**: `git init`
* **Clonar Repositorio**: `git clone <url>`
* **Revisar el historial de cambios**: `git log`
* **Cambiar el estado al commit padre**: `git checkout HEAD^`
* **Deshacer cambios (y perderlos)**: `git reset --hard`
* **Agregar carpeta `a` y su contenido a `staging`**: `git add a`
* **Crear un `commit` con los cambios en `staging` y el mensaje `commit message`**: `git commit -m "commit message"`


#### Explorar historial de cambios

La forma más fácil de hacerlo es con un programa de interfaz gráfica, como por ejemplo, `gitk`. En clases veremos cómo usar este programa.

## Almacenamiento en Linux

En esta parte del apunte hablaremos un poco acerca del manejo de dispositivos de almacenamiento en Linux. También mostraremos algunos comandos para ejecutar tareas básicas para crear, listar y borrar particiones.

### Conceptos Generales

* **Dispositivo de Almacenamiento Secundario**: Cualquier dispositivo que permita almacenar información de forma persistente. Algunos ejemplos de este tipo de dispositivos son los discos duros, las unidades de estado sólido (SSD), las tarjetas flash (SD, MMC, cartuchos de videojuegos), diskettes, CDs (no permiten reescritura), DVDs, etc.
* **Tabla de Particiones**: Un dispositivo de almacenamiento secundario puede dividirse en una o más unidades lógicas de almacenamiento, las cuales se conocen como particiones. La cantidad de particiones y su ubicación en el espacio físico de almacenamiento se definen en la **tabla de particiones**. Las siguientes son tipos de tablas de particiones comunes:
  * **MBR**: (Master boot record) Tabla de particiones usada en versiones antiguas de Windows y Linux. Tenía varias limitaciones, como tamaño máximo de particiones y cantidad de particiones por disco.
  * **GPT**: (GUID Partition Table) Tabla de particiones usada en computadores modernos con Windows y Linux. Es más 
* **Sistemas de Archivos**: Guardar información en un dispositivo de almacenamiento no es una tarea directa. En general, aparte de la información a guardar, uno desea guardar metainformación extra asociada a cada archivo, como nombre, fecha de creación o modificación, propietario, permisos, ubicación, etc. Al mismo tiempo, uno podría querer que el mismo dispositivo se encargue de algunas tareas comunes, como llevar respaldo de los archivos a medida se modifican u optimizar el uso de espacio en casos en que hay mucha información redundante. Este tipo de funcionalidades se pueden definir a nivel del sistema de archivos asociado a la partición. Algunos sistemas de archivos conocidos son:
  * **FAT, FAT12, FAT16, FAT32 y exFAT**:  File Allocation Table es un sistema de archivos creado a fines de los años 70. Cada versión mencionada se diferencia en el tamaño máximo de los archivos que puede almacenar y del tamaño máximo de la partición. FAT32 soporta volúmenes de hasta 2 TeraBytes, mientras que exFAT soporta hasta 128 PetaBytes.
  * **NTFS**: Sistema de Archivos propietario de Microsoft y usado principalmente en la familia de sistemas operativos Windows NT. Soporta una mayor cantidad de metadatos, el uso de listas de control de acceso y el uso de [Journaling](https://en.wikipedia.org/wiki/Journaling_file_system) para evitar errores de escritura.
  * **ext2, ext3 y ext4**: Sistemas de archivos usados en Linux principalmente. ext3 y ext4 se caracterizan por ser  _journaled_. Las versiones más nuevas soportan además volúmenes más grandes.
  * **ZFS**: Sistema de archivos con hartas características que lo hacen ideal para el manejo de respaldos o grandes volúmenes de datos.
  * **BTRFS**: Sistema de archivos con capacidades de integridad y respaldo de archivos.
  * **HFS, HFS+ y APFS**:  Sistemas de archivos usados principalmente en sistemas operativos OSX/macOS. HFS+ y APFS son _journaled_. APFS posee funcionalidades de respaldos, cifrado, optimizaciones para SSDs y revisión de integridad de archivos como parte de las funcionalidades básicas del sistema de archivos.

* **Montar/Desmontar un sistema de archivos**: Para utilizar un sistema de archivos en Linux, es necesario montarlo en una carpeta del sistema. Luego de hacerlo, los archivos del sistema de archivos se verán en esa carpeta.

* **_Block Devices_**: En Linux, varios dispositivos se comportan como si fueran archivos en el sistema. En el caso de los dispositivos de almacenamiento, estos se suelen mostrar como dos tipos de archivos. En la práctica, los _Block Devices_ permiten leer y escribir directamente de o en los dispositivos de almacenamiento. Por ejemplo, si quisiera copiar un disco completo identificado en el sistema como el archivo `/dev/sda`, basta con _copiar_ esa ruta por completo (con un comando especial). Lo mismo si quisiera cargar un respaldo en un disco (debo _escribir_ en ese archivo la imagen de respaldo).

* **Dispositivos loop**: Son seudo dispositivos de almacenamiento, los cuales permiten hacer que un archivo común y corriente actúe como un dispositivo de bloques. Si se montan con un comando especial, aparecerán como dispositivos de bloque.

### Herramientas útiles
* `lsblk`: Muestra todos los dispositivos de almacenamiento de bloque en el sistema.
* `gparted`: Permite crear particiones con una interfaz gráfica muy simple de usar.
* `gnome-disks`: Permite revisar dispositivos de almacenamiento conectados, crear imágenes de ellos y montar imágenes virtuales. También tiene funcionalidades limitadas para formatear y crear particiones y tablas de particiones.
* `dd`: Permite copiar a bajo nivel información de sistemas de archivos en respaldos u otros sistemas de archivos. Debido a que trabaja en muy bajo nivel (byte a byte en el dispositivo), su mal uso puede ser muy peligroso.
  * Ej: `dd if=/dev/sda of=backup.img status=progress`: Copia el dispositivo de bloque `/dev/sda` al archivo backup.img
* `losetup`: Permite configurar _loop devices_:
  * Ej: `sudo losetup /dev/loop0 backup.img` transforma la imagen en un dispositivo _loop_. 
* `mount`: Permite montar un sistema de archivos en una carpeta.
  * Ej: `sudo mount /dev/sda /mnt` Monta el dispositivo de bloque `/dev/sda` en la carpeta `/mnt`
* `umount`: Permite desmontar una carpeta a la que previamente se le montó un sistema de archivos.
  * Ej: `sudo umount /dev/sda` desmonta el dispositivo de bloque `/dev/sda`.
  * Ej2: `sudo umount /mnt` desmonta el dispositivo de bloque que se montó previamente en `/mnt`.

## Recuperación de archivos

En problemas de forense, puede que sea necesario tratar con soportes de almacenamiento dañados o con archivos borrados. A continuación se nombran algunos de estos problemas posibles y qué programas podemos usar para resolverlos.

### Problemas recurrentes

* **Recuperación de Archivos dañados**: Es posible que contemos con uno o más archivos dañados, y queramos repararlos para acceder de forma parcial o total a su contenido. Para lo anterior, sería necesario un programa especializado para el tipo de archivo, que aproveche algunas de las propiedades del formato para recuperar la información. Cabe destacar que no todos los tipos de archivos son reparables o recuperables con estos métodos, y en general es muy probable que parte de la información se corrompa.
* **Recuperación de Archivos Eliminados**: Cuando se elimina un archivo de un soporte de almacenamiento, en general no se borra, sino que se elimina de un _índice_ del mismo soporte. Si escaneáramos byte a byte el soporte de almacenamiento, existe la posibilidad de recuperar el archivo de forma total o parcial, siempre y cuando ese espacio de memoria no haya sido sobreescrito por otro archivo.
* **Uso de Archivos Temporales para recuperar información**: Algunos programas de edición de archivos guardan versiones temporales de estos en carpetas especiales. En algunos casos es posible recuperar el contenido de un documento importante a partir de los archivos temporales. 
* **Reparación de componentes físicas del dispositivo de almacenamiento**: En casos más complejos, es posible que el soporte de almacenamiento se encuentre dañado físicamente. El daño podría ser bajo, como por ejemplo, sectores del disco duro ilegibles. Sin embargo, también podría extenderse de tal forma que el dispositivo no es reconocible por el sistema operativo. En el primer caso, muchas veces es posible reparar el sistema de archivos de forma manual. En el segundo caso, puede ser necesario incluso contratar servicios de recuperación de datos especializados.
* **Reparación de sistemas de archivos**: A veces el daño no ocurre a nivel de hardware, sino que está relacionado con los datos almacenados en el soporte que identifican el contenido dentro del dispositivo. Por ejemplo, podría dañarse el índice del disco o su tabla de particiones, para lo cual se requeriría regenerarla o repararla para poder acceder a su contenido.

### Herramientas

* [**Testdisk** (Linux, software libre)](https://www.cgsecurity.org/wiki/TestDisk)
* [**ddrescue** (GNU/Linux, software libre)](https://www.gnu.org/software/ddrescue/)
* [**FSCK** (Linux, software libre)](https://en.wikipedia.org/wiki/Fsck)
* [**CHKDSK** (Windows)](https://en.wikipedia.org/wiki/CHKDSK)
* [**Recuva** (Windows, software privativo)](https://www.ccleaner.com/recuva)


## Imágenes Forenses

En casos más realistas, es posible que se les proporcionen imágenes forenses tanto de discos duros/SSDs como de memoria RAM. Estas imágenes pueden ser creadas y revisadas con aplicaciones especiales. Algunas son comerciales, como [EnCase Forensic](https://www.opentext.com/products/encase-forensic), mientras que otras son abiertas o gratuitas:

* [**FTK Imager**](https://www.exterro.com/digital-forensics-software/ftk-imager) Herramienta popular utilizada para generar y revisar imágenes forenses (extensión .E01)
* [**Volatility** (Multiplataforma, Open source)](https://volatilityfoundation.org/) Herramienta en Python para revisar y explorar imágenes de memoria RAM. Existen dos versiones de uso común (Volatility 2 y Volatility 3), cada una con plugins específicos.
* [**Autopsy** (Linux y Windows)](https://github.com/sleuthkit/autopsy) Permite abrir imágenes forenses generadas por FTK Imager y otras aplicaciones (contando con los plugins adecuados)
* [**Linux Memory Extractor (LiME)**](https://github.com/504ensicsLabs/LiME) Herramienta para extraer una imagen de memoria de un dispositivo con kernel de Linux compatible.
