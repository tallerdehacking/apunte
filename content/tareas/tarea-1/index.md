---
title: "Tarea 1 2021/1"
description: "Stego y Criptografía Moderna"
date: 2021-04-11T09:19:42+01:00
draft: false
weight: 50
---

# Tarea 1

## Indicaciones generales

* Cuentan con **4 semanas** para desarrollar y ejecutar esta tarea desde el día de su lanzamiento.
* La ejecución de esta tarea es **grupal**, con el grupo armado a inicios del curso.
* Se requiere que cada integrante del grupo esté "a cargo" de un problema de los entregados. Se debe explicitar el problema del cual cada integrante esté a cargo.
* Dentro de un mismo grupo, **se pueden discutir libremente los problemas durante la ejecución de la tarea**. Sin embargo, **los problemas no se pueden discutir entre integrantes de grupos distintos, salvo en situaciones guiadas por el equipo docente en bloque de clase** (como por ejemplo, horarios de consultas en auxiliares o cátedras).

## Modo de entrega

* Cada estudiante debe entregar individualmente los siguientes archivos para cada problema de la tarea:
    * Un archivo en Markdown que explique cómo resolvió el problema (_Writeup_), detallando todos los pasos ejecutados como para que al replicarlos se pueda llegar a la misma solución. Su formato debe ser idéntico al del _Formato de Writeup_ adjunto al final de esta sección.
    * Archivos de código si es que eran necesarios para resolverlo.
    * Enlaces a todas las herramientas usadas.
* Al inicio del archivo Markdown mencionado anteriormente, debe escribir su nombre, su grupo y si era o no la persona encargada de resolver ese problema. 
* También debe entregar una solución con código y _Writeup_ para todos los problemas en los que no estuvo encargado.

[Formato de Writeup](./writeup.txt)

## Problemas

### P1: Speak friend

En su travesía a Mordor, la Comunidad del Anillo debe pasar por Khazad-dûm. Sin embargo, han encontrado con un obstáculo que no les permite continuar. 
¿Puedes ayudarlos a abrir las puertas y continuar su camino a destruir el anillo?

[Archivo](./p1_speak.txt)


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

[Mensaje Cifrado](./p2_ciphered.txt)

## P3: En Construcción

😲