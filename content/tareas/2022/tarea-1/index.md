---
title: "Tarea 1 2022/1"
description: "Stego y Criptografía Moderna"
date: 2022-04-01T09:19:42+01:00
draft: false
weight: 50
---
## Indicaciones generales

* Cuentan con **3 semanas** para desarrollar y ejecutar esta tarea desde el día de su lanzamiento. Revisen U-Cursos para ver la fecha de entrega más actualizada.
* La ejecución de esta tarea es **grupal**, con el grupo armado a inicios del curso.
* Se requiere que cada integrante del grupo esté "a cargo" de un problema de los entregados. Se debe explicitar el problema del cual cada integrante esté a cargo.
* Dentro de un mismo grupo, **se pueden discutir libremente los problemas durante la ejecución de la tarea**. Sin embargo, **los problemas no se pueden discutir entre integrantes de grupos distintos, salvo en situaciones guiadas por el equipo docente en bloque de clase** (como por ejemplo, horarios de consultas en auxiliares o cátedras).

## Modo de entrega

* **Cada estudiante** debe entregar **individualmente** los siguientes archivos para cada problema de la tarea:
    * Un archivo en Markdown que explique cómo resolvió el problema (_Writeup_), detallando todos los pasos ejecutados como para que al replicarlos se pueda llegar a la misma solución. Su formato debe ser idéntico al del _Formato de Writeup_ adjunto al final de esta sección.
    * Archivos de código si es que eran necesarios para resolverlo.
    * Enlaces a todas las herramientas usadas.
* Al inicio del archivo Markdown mencionado anteriormente, debe escribir su nombre, su grupo y si era o no la persona encargada de resolver ese problema. 
* Recuerden que también deben entregar una solución con código y _Writeup_ para todos los problemas en los que no estuvieron encargados.

[Formato de Writeup](./writeup.txt)

[Cómo se ve al exportarlo en Joplin](./writeup.pdf)

## Problemas

### P1: Censura

El grupo hacktivista Th3_0ffi5 cifró todos los archivos de nuestra papelería.

Un informante anónimo dejó pistas para recuperar la llave de descifrado, pero el audio se corrompió :(

¿Nos ayudas a recuperar la información dentro de nuestros documentos?

_(Esto no hubiese pasado si estuviesen impresos en papel :()_

[Descargar Archivos](../p1.zip)

### P2: BinAES

Es AES, pero para datos en binario.

Seguridad y minimalismo. ¿Así funciona, verdad?

¡Nunca sabrás que dice el archivo cifrado!

Servidor: `5.161.93.52:25101` (Recuerda conectarte a la VPN del CEC)

[Archivo cifrado](../p2.txt)

## P3: PlayStation

Luego del [Incidente de 2010](https://www.youtube.com/watch?v=HEFMAP0mTvY), la persona a cargo del desarrollo criptográfico que trabajaba en la división de videojuegos de Sony se fue a trabajar a un la Casa de Moneda de nuestro país (no confundir con La Moneda).

Sabemos que reusó algo del código de Sony en la implementación de firma electrónica usada en donde trabaja. Sabemos también que suele reusar sus llaves privadas.

Nos conseguimos código interno relacionado a firmas, dos firmas con sus archivos respectivos y un archivo cifrado que sabemos tiene algo valioso.

¿Nos ayudas a descifrar el archivo?