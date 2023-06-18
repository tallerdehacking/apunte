---
title : "Intro a Hardware"
lead: ""
date: 2023-06-14T09:25:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "hardware"
weight: 010

---

Hoy en día estamos rodeados de dispositivos con la capacidad de recibir y transmitir
información. Desde electrónicos simples, como sensores de luz, hasta dispositivos
altamente integrados y complejos, como teléfonos celulares. Cada uno de estos requiere
de un programa o software que le otorgue su funcionamiento básico, además de instrucciones sobre
cómo leer y enviar información. En este capítulo veremos problemas de Hardware,
que tratan de aprovecharse de ciertas fallas o ausencia de mecanismos de seguridad
en los dispositivos.

Si bien los problemas de Hardware están basados en Hardware Hacking
(y muchas de las herramientas y técnicas utilizadas para estos problemas también sirven para eso),
no es necesario tener hardware ni hackear hardware físicamente para resolverlos.
Estos usualmente se basan en analizar el firmware de algún dispositivo, como un IoT,
o decodificar información enviada a través de un canal de transmisión interceptado,
como los cables entre un controlador y una pantalla LCD.

Al igual que todos los temas que hemos visto en este ramo, los problemas de Hardware
pueden ser muy amplios y abarcar múltilpes técnicas, requiriendo conocimientos
de muchas áreas. Nosotros nos centraremos en 2 cosas:

1. Reversing de _firmware_: Analizar el código básico que corre un dispositivo
para encontrar fallas de seguridad en este.
2. Decodificar los protocolos de comunicación serial: Leer la información
enviada entre dispositivos a través de cables o bus de comunicación.

En la práctica, estas dos técnicas suelen utilizarse en conjunto; se conecta directamente
a la interfaz serial (por ejemplo UART) del dispositivo que se quiere hackear,
con lo cual se fuerza un dump del _firmware_. Luego, se analiza este _firmware_
para encontrar vulnerabilidades y luego explotarlas en el dispositivo mismo. 

Por restricciones de tiempo, hay muchas cosas que no veremos en este ramo. Por ejemplo
decodificar ondas de radio, leer el protocolo USB, explotar PLCs, entre muchos otros.
