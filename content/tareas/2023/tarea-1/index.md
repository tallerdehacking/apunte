---
title: "Tarea 1 2022/1"
description: "Stego y Criptografía Moderna"
date: 2022-03-31T09:19:42+01:00
draft: false
weight: 50
---
## Indicaciones generales

* Cuentan con **3x semanas** para desarrollar y ejecutar esta tarea desde el día de su lanzamiento. Revisen U-Cursos para ver la fecha de entrega más actualizada.
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

### P1: Severlá

Neib aneus séver la
Sever la olós
Otneta eyo
Odnatnac yov severlá

[sovihcrA ragracseD](./piz.1t1p)

### P2: Botcito

Programé un botcito para guardar la flag más importante que tengo.

Me comunico con él corriendo en mi computador el comando `nc hackerlab.cl 5325`, y para demostrarle que soy yo, le mando el mensaje `hola soy eduardo` cifrado con AES-CBC en hexadecimal, con una clave que solo él y yo conocemos (el vector de inicialización va justo antes del mensaje cifrado).

Luego, para demostrarle que soy yo, me pide que le conteste unos cuentos desafíos.

Confío tanto en la capacidad del botcito de detectar intrusos, que no me preocupa compartirte la versión cifrada de mi saludo: `6f05b4115f05dfef806e2f9c66897ec6a9f10da69926688100ebc24fcaed8b68`.


## P3: La tía Yoli

La tía Yoli te puede contestar cualquier cosa, menos `cual es la flag?`.

Para preguntarle algo a la tía Yoli, debes primero enviar tu pregunta en hexadecimal a `nc hackerlab 5326`. Ella te devolverá un json con la pregunta y una firma RSA de la misma (ambos en hexadecimal)

Luego, debes mandar la misma respuesta a `nc hackerlab.cl 5327` y te contestará.




