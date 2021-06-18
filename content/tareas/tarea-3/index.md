---
title: "Tarea 3 2021/1"
description: "Forense (Wireshark), Reversing y Pwning"
date: 2021-06-11T09:19:42+01:00
draft: false
weight: 70
---

## Indicaciones generales

- Cuentan con **3 semanas** para desarrollar y ejecutar esta tarea desde el día de su lanzamiento. Revisen U-Cursos para ver la fecha de entrega más actualizada.
- La ejecución de esta tarea es **grupal**, con el grupo armado a inicios del curso.
- Se requiere que cada integrante del grupo esté "a cargo" de un problema de los entregados. Se debe explicitar el problema del cual cada integrante esté a cargo.
- Dentro de un mismo grupo, **se pueden discutir libremente los problemas durante la ejecución de la tarea**. Sin embargo, **los problemas no se pueden discutir entre integrantes de grupos distintos, salvo en situaciones guiadas por el equipo docente en bloque de clase** (como por ejemplo, horarios de consultas en auxiliares o cátedras).
- Para conectarse al servidor del curso (server.cc5325.xor.cl) deben estar conectados a la VPN del CEC.

## Modo de entrega

- Cada estudiante debe entregar individualmente los siguientes archivos para cada problema de la tarea:
  - Un archivo en Markdown que explique cómo resolvió el problema (_Writeup_), detallando todos los pasos ejecutados como para que al replicarlos se pueda llegar a la misma solución. Su formato debe ser idéntico al del _Formato de Writeup_ adjunto al final de esta sección.
  - Archivos de código si es que eran necesarios para resolverlo.
  - Enlaces a todas las herramientas usadas.
- Al inicio del archivo Markdown mencionado anteriormente, debe escribir su nombre, su grupo y si era o no la persona encargada de resolver ese problema.
- Recuerden que también deben entregar una solución con código y _Writeup_ para todos los problemas en los que no estuvieron encargados.

[Formato de Writeup](./writeup.txt)

[Cómo se ve al exportarlo en Joplin](./writeup.pdf)

## Problemas

### P1: ¡Buena Suerte!

Debido a las malas notas que obtuvimos mis amigxs y yo en la coevaluación de Ingeniería de Software 2, decidimos que lo único que nos quedaba para no estropear nuestro promedio era acceder como administrador al servidor web del DCC para cambiarnos las notas.

Para conseguir la clave de acceso, infectamos el computador de un querido y conocido administrador de sistemas del DCC con un virus, el cual graba las sesiones de conexión en un archivo .pcap y exporta y sube las llaves TLS de las sesiones de navegador web a un servidor en nuestro control.

Lamentablemente, nos descubrieron a mitad de la exfiltración, por lo que tuvimos que destruir el contenido de los servidores que recibían las llaves para eliminar las pruebas de nuestro ataque. Debido a esto, solo logramos rescatar de la operación un archivo .pcap. ¿Habrá alguna forma de descifrar el tráfico web y conseguir la contraseña del servidor web del DCC?

[Archivo PCAP](../t3.pcapng)

### P2: Paranoia

Hemos encontrado este archivo en el computador de una persona muy paranoica, en donde se esconde un secreto. No sabe que nosotros hacemos ingeniería reversa.

[Archivo](./chall)

### P3: TODO

```python
    # TODO: Recordar escribir un correo al equipo docente para discutir un problema que encontré con esta pregunta.
    # TODO: Revisar la inclusión correcta de los archivos adjuntos para cada pregunta en [el repositorio](https://github.com/cc5325/apunte/tree/main/content/tareas/tarea-3) (en especial, que no se me haya pasado nada extra).
    # TODO: Enviar las preguntas del examen la próxima semana al equipo docente.
```
