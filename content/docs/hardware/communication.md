---
title : "Protocolos de Comunicación"
lead: ""
date: 2023-06-14T09:25:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "hardware"
weight: 802

---

## Protocolos

A continuación veremos cómo funcionan ciertos protocolos de comunicación serial.
Estos se utilizan para comunicar dispositivos directamente, mediante un bus de datos.
El bus de datos suele tomar la forma de cables conectando directamente a los dispositivos,
y cumlpen ciertas condiciones para lograr establecer la comunicación.

### UART

Uno de los protocolos de comunicación de bajo nivel más utilizados y antiguos es
el _Universal Asynchronous Receiver - Transmitter_ (**UART**).
Es un tipo de comunicación serial y bidireccional (_full-duplex_) entre 2 dispositivos,
utilizando únicamente 2 cables: _Transmitter_ (Tx) y _Receiver_ (Rx).
Notar que el Tx de un dispositivo es el Rx del otro, y viceversa.

![UART](../uart.png)

La frecuencia de transmisión, llamada _Baud rate_ y medida en _bits-per-second_ (bps),
debe acordarse previamente entre los dispositivos.
En teoría no hay restricciones (aparte de físicas) en la frecuencia que pueden tomar,
pero en la práctica hay tan solo unas pocas frecuencias que se utilizan:
1200, 2400, 4800, 9600, 19200, 38400, 57600, y 115200 bps. Dentro de estas,
9600 bps es la más común.

Los datos se envían en _frames_ de entre 5 y 9 bits. Cada _frame_ lleva adicionalmente
bits de inicio y término, y opcionalmente un bit de paridad. El flujo completo es el siguiente:

1. Bit de inicio (_start bit_): Indica el inicio de una transmisión.
2. Bits de datos (_data bits_): Entre 5 y 9 bits con los datos transmitidos.
3. Bit de paridad (_parity bit_, opcional): Indica la paridad de los bits de datos.
Se utiliza para detectar cambios en la transmisión.
4. Bit de término (_stop bit_): Indica el fin de una transmisión.

Se envía tantos _frames_ como sea necesario para transmitir toda la información.
Cada _frame_ enviado puede representar un caracter, un número, o incluso
datos binarios. La siguiente imagen, obtenida de
[Wikipedia](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter),
explica bastante bien el proceso. Notar que el BCLK es la frecuencia de transmisión
acordada previamente entre los dispositivos.

![UART Signal](../uart-signal.png)

### I2C

_Inter-Integrated Circuit_ (**I2C**) también utiliza 2 cables, pero este protocolo
es solo _half-duplex_. Es decir que los dispositivos deben tomar turnos para transmitir.
Adicionalmente, se permiten más de dos dispositivos conectados, con uno funcionando
como transmisor y el resto como receptores.

Para la comunicación, la información es enviada a través de la línea de datos SDA,
mientras que el reloj que coordina a los dispositivos se transmite en la línea SCL.
Luego, y a diferencia de UART, no se necesita información adicional para establecer
la comunicación.

![I2C](../i2c.png)

Dado que I2C utiliza solo un canal para la comunicación entre múltiples dispositivos,
el protocolo es un poco más complejo que UART. Requiere de secuencias de sincronización
para determinar quién puede transmitir en cada momento, bytes de ACK y NACK,
para indicar si se recibió correctamente cada parte del mensaje, direcciones de destino,
para saber a cuál de los dispositivos se está transmitiendo, entre otras cosas.
No entraremos en más detalle para este protocolo, dado que puede variar significativamente
entre implementaciones.

### SPI

Por último, tenemos el _Serial Peripheral Interface_ (**SPI**), también llamado
_four-wire serial bus_ (bus de comunicación de cuatro cables), el cual fue diseñado
para comunicación a distancias cortas. Este permite una transferencia de datos
mucho más alta que los protocolos anteriores, de aproximadamente 250 Mbps.
La comunicación es de tipo síncrona, _full-duplex_ y permite a más de dos dispositivos
conectados, pero por simplicidad, solo veremos el caso de un _master_ y un _slave_.

El protocolo requiere de cuatro señales para establecer comunicación:
* **SCLK**: _Serial Clock_, señal de reloj utilizada para sincronizar los dispositivos.
* **MOSI**: _Master Out Slave In_, los datos enviados desde el controlador (_master_),
hacia el dispositivo periférico (_slave_).
* **MISO**: _Master In Slave Out_, los datos enviados desde el dispositivo periférico
hacia el controlador.
* **SS**: _Slave Select_, funciona como una señal de _enable_. Le indica al
dispositivo periférico que el controlador está enviando datos.

![SPI](../spi.png)

La transmisión de datos suele consistir en palabras (_words_) de 8 bits,
aunque algunos dispositivos soportan hasta 12 o 16 bits. A diferencia de UART,
SPI no requiere de bits de inicio ni término de la transmisión, lo que le permite
una mayor densidad de datos transmitidos. Tampoco interrumpe la transmisión para
verificar la recepción ni para coordinar a los dispositivos. Esto último puede
significar que el controlador transmita al vacío sin saberlo.

Debido a la alta flexibilidad de SPI, no existe una única forma de transmitir
la información. Esto es altamente dependiente de la implementación en particular,
y los datos pueden ir codificados de diferentes formas. Debido a esto, no entraremos
en más detalle sobre el protocolo.

## Herramientas

Para efectos de este ramo, utilizaremos las herramientas desarrolladas por
[Saleae](https://www.saleae.com/) para decodificar y leer señales UART, I2C y SPI.
Existen otras herramientas con diferentes funcionalidades, capacidades y propósitos,
pero no serán necesarias para este curso. Estas herramientas permiten decodificar
directamente la información enviada por medio de los protocolos mencionados
anteriormente, extrayendo automáticamente el mensaje.

### Logic 1

[Logic 1](https://support.saleae.com/logic-software/legacy-software/older-software-releases)
es una herramienta de legado, la cual ya no se actualiza.
Sin embargo, sirve para leer y visualizar archivos `.logicdata`.
Las funcionalidades de esta versión son relativamente limitadas, pero permite trabajar con
diferentes tipos de señales.

Como ejemplo, decodificaremos una señal I2C usando Logic 1. Primero abrimos el
archivo `.logicdata` usando Logic 1.

![Logic 1 I2C 1](../logic1-i2c1.png)

Seleccionamos el _analyzer_ de I2C.

![Logic 1 I2C 2](../logic1-i2c2.png)

Lo configuramos de la siguiente manera. Sabemos previamente que las direcciones son
solo de 7 bits, por lo que usamos esa configuración.

![Logic 1 I2C 3](../logic1-i2c3.png)

Finalmente, exportamos el resultado. En este caso no tienen mucho sentido los datos,
dado que deben ser procesados luego de la exportación.

![Logic 1 I2C 4](../logic1-i2c4.png)

### Logic 2

[Logic 2](https://www.saleae.com/downloads/) es la versión soportada del software,
y lee archivos `.sal`.
Los desarrolladores de Saleae no disponen de una herramienta para exportar
ni convertir formatos entre las versiones de su software.
Esta versión cuenta con muchas más funcionalidades que Logic 1;
permite instalar extensiones, realizar análisis más complejos,
visualizar los datos de una mejor manera, entre otras cosas.

A continuación analizaremos el contenido de una transmisión UART. En este caso
solo tenemos los datos enviados a través de un cable y no conocemos el _baud rate_.
Primero abrimos Logic 2 e importamos el archivo `.sal`.

![Logic 2 UART 1](../logic2-uart1.png)

De ser necesario, instalamos las extensiones _Baud rate estimate_ y _UART HIC Decoder_
de la pestaña de extensiones.

![Logic 2 UART 2](../logic2-uart2.png)

Luego, vamos a la pestaña de mediciones y medimos la señal completa, para encontrar
que el _baud rate_ estimado es de 31.23 kHz.

![Logic 2 UART 3](../logic2-uart3.png)

Finalmente, vamos a la pestaña de _analyzers_, y seleccionamos un _async serial_.

![Logic 2 UART 4](../logic2-uart4.png)

Lo configuramos con la frecuencia que encontramos y usamos los valores estándar
para el resto de los parámetros.

![Logic 2 UART 5](../logic2-uart5.png)

Con esto logramos decodificar la señal y obtener su contenido. Los datos pueden
ser exportados a un archivo CSV o copiados directamente del programa.

![Logic 2 UART 6](../logic2-uart6.png)
