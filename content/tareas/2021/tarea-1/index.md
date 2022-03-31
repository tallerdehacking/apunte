---
title: "Tarea 1 2021/1"
description: "Stego y Criptografía Moderna"
date: 2021-04-11T09:19:42+01:00
draft: false
weight: 50
---
## Indicaciones generales

* Cuentan con **4 semanas** para desarrollar y ejecutar esta tarea desde el día de su lanzamiento. Revisen U-Cursos para ver la fecha de entrega más actualizada.
* La ejecución de esta tarea es **grupal**, con el grupo armado a inicios del curso.
* Se requiere que cada integrante del grupo esté "a cargo" de un problema de los entregados. Se debe explicitar el problema del cual cada integrante esté a cargo.
* Dentro de un mismo grupo, **se pueden discutir libremente los problemas durante la ejecución de la tarea**. Sin embargo, **los problemas no se pueden discutir entre integrantes de grupos distintos, salvo en situaciones guiadas por el equipo docente en bloque de clase** (como por ejemplo, horarios de consultas en auxiliares o cátedras).

## Modo de entrega

* Cada estudiante debe entregar individualmente los siguientes archivos para cada problema de la tarea:
    * Un archivo en Markdown que explique cómo resolvió el problema (_Writeup_), detallando todos los pasos ejecutados como para que al replicarlos se pueda llegar a la misma solución. Su formato debe ser idéntico al del _Formato de Writeup_ adjunto al final de esta sección.
    * Archivos de código si es que eran necesarios para resolverlo.
    * Enlaces a todas las herramientas usadas.
* Al inicio del archivo Markdown mencionado anteriormente, debe escribir su nombre, su grupo y si era o no la persona encargada de resolver ese problema. 
* Recuerden que también deben entregar una solución con código y _Writeup_ para todos los problemas en los que no estuvieron encargados.

[Formato de Writeup](./writeup.txt)

[Cómo se ve al exportarlo en Joplin](./writeup.pdf)

## Problemas

### P1: Speak friend

En su travesía a Mordor, la Comunidad del Anillo debe pasar por Khazad-dûm. Sin embargo, han encontrado con un obstáculo que no les permite continuar. 
¿Puedes ayudarlos a abrir las puertas y continuar su camino a destruir el anillo?

[Archivo](./p1.zip)

**Nota:** Esta flag no contiene la estructura `CC5325{FLAG}` al encontrarla. Sabrán cual es la flag porque el mismo texto se los indicará.

### P2: Morsifrador

Interceptamos un mensaje en código Morse de un equipo competidor, pero cifrado con una clave
y un modo desconocidos.

El mensaje en texto plano está compuesto de estas cuatro "unidades", concatenadas sin espacios entre ellas:

- DITT: Representa un punto (`.`) en código Morse.
- DASH: Representa un guión (`-`) en código Morse.
- SPCE: Representa el final de un caracter en código Morse.
- SLSH: representa el final de una palabra en código Morse.

Ejemplo: El texto plano de `hola mundo` sería `DITTDITTDITTDITTSPCEDASHDASHDASHSPCEDITTDASHDITTDITTSPCEDITTDASHSLSHDASHDASHSPCEDITTDITTDASHSPCEDASHDITTSPCEDASHDITTDITTSPCEDASHDASHDASH` en esta codificación. (No es muy eficiente, ¿cierto?)

Mediante una operación de ciberinteligencia también identificamos un servicio expuesto por ellos,
el cual cifra los mensajes en texto plano que se le envíen (considerando los tamaños de salida,
el servicio no los codifica en código Morse). Este servicio lo pueden encontrar en `server.cc5325.xor.cl`,
puerto `25102` y pueden usarlo sin preocupaciones, ya que no parece estar monitoreado.

Requerimos que descifren el mensaje adjunto interceptado por nuestro equipo, y nos indiquen qué es
lo que trama el equipo competidor.

**Hint**: _Partan analizando el servicio que encontramos y cifra los mensajes. ¿Qué pueden descubrir
de la codificación utilizada?_

**Nota:** Recuerden estar conectados a la VPN del CEC.


[Mensaje Cifrado](./p2.txt)

## P3: DesesperanRSA

La flag se perdió para siempre 😥 La ciframos para evitar que se la robaran, pero la llave privada que usamos para cifrarla se perdió cuando formateamos el pendrive que mantenía su única copia.

No te molestes en intentar encontrar la flag. Está cifrada con RSA de 2048 bits y perdida en un millar de frases sin sentido.

Pero bueno, lo último que se pierde es la esperanRSA.

[Código fuente y mensaje cifrado](./p3.zip)
