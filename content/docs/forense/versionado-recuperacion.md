---
title : "Versionado y Recuperación de Archivos"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "forense"
weight: 030

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

## Recuperación de archivos

En problemas de forense, puede que sea necesario tratar con soportes de almacenamiento dañados o con archivos borrados. A continuación se nombran algunos de estos problemas posibles y qué programas podemos usar para resolverlos.

### Problemas recurrentes

* **Recuperación de Archivos dañados**: Es posible que contemos con uno o más archivos dañados, y queramos repararlos para acceder de forma parcial o total a su contenido. Para lo anterior, sería necesario un programa especializado para el tipo de archivo, que aproveche algunas de las propiedades del formato para recuperar la información. Cabe destacar que no todos los tipos de archivos son reparables o recuperables con estos métodos, y en general es muy probable que parte de la información se corrompa.
* **Recuperación de Archivos Eliminados**: Cuando se elimina un archivo de un soporte de almacenamiento, en general no se borra, sino que se elimina de un _índice_ del mismo soporte. Si escaneáramos byte a byte el soporte de almacenamiento, existe la posibilidad de recuperar el archivo de forma total o parcial, siempre y cuando ese espacio de memoria no haya sido sobreescrito por otro archivo.
* **Uso de Archivos Temporales para recuperar información**: Algunos programas de edición de archivos guardan versiones temporales de estos en carpetas especiales. En algunos casos es posible recuperar el contenido de un documento importante a partir de los archivos temporales. 
* **Reparación de componentes físicas del dispositivo de almacenamiento**: En casos más complejos, es posible que el soporte de almacenamiento se encuentre dañado físicamente. El daño podría ser bajo, como por ejemplo, sectores del disco duro ilegibles. Sin embargo, también podría extenderse de tal forma que el dispositivo no es reconocible por el sistema operativo. En el primer caso, muchas veces es posible reparar el sistema de archivos de forma manual. En el segundo caso, puede ser necesario incluso contratar servicios de recuperación de datos especializados.
* **Reparación de sistemas de archivo**: A veces el daño no ocurre a nivel de hardware, sino que está relacionado con los datos almacenados en el soporte que identifican el contenido dentro del dispositivo. Por ejemplo, podría dañarse el índice del disco o su tabla de particiones, para lo cual se requeriría regenerarla o repararla para poder acceder a su contenido.

### Herramientas

* [**Testdisk** (Linux, software libre)](https://www.cgsecurity.org/wiki/TestDisk)
* [**ddrescue** (GNU/Linux, software libre)](https://www.gnu.org/software/ddrescue/)
* [**FSCK** (Linux, software libre)](https://en.wikipedia.org/wiki/Fsck)
* [**CHKDSK** (Windows)](https://en.wikipedia.org/wiki/CHKDSK)
* [**Recuva** (Windows, software privativo)](https://www.ccleaner.com/recuva)

## Otros tipos de recuperación de información

Lamentablemente, en el curso no alcanzaremos a ver los siguientes conceptos. Sin embargo, les dejamos algunas referencias para que, en caso que les interesen, los puedan ver por su cuenta:

* **Recuperación de información en RAM**: La memoria RAM en un computador se destaca por ser de rápido acceso (comparada con la memoria secundaria), pero volátil. Al cortar la energía del computador, los datos almacenados en RAM se pierden en forma parcial o total. En los casos en los que se requiera recuperar información presente en RAM, suele generarse una imagen del estado completo del sistema (almacenamiento secundario y RAM), para posteriormente analizarla con mayor tranquilidad. 
* **Recuperación de información en máquinas virtuales**: En algunos problemas de CTF, se entregan imágenes del estado completo de una máquina virtual, las cuales contienen fundamentalmente la RAM del sistema al momento de estar ejecutándose. Existen programas especiales para revisar esta información.

