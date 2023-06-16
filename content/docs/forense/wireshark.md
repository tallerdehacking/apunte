---
title: "Wireshark"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "forense"
weight: 404
---

Algunos problemas de tipo CTF de categoría forense requieren analizar logs de tráfico de red, los cuales suelen guardarse con la aplicación Wireshark. En esta sección describiremos brevemente algunos conceptos relacionados con el modelo de Internet y luego explicaremos algunas funcionalidades de Wireshark.

## Modelo de Internet

Tambien conocido como Modelo TCP/IP, considera varios componentes que permiten el intercambio de información entre dispositivos conectados a una red.

Las capas del modelo son las siguientes:

- **Capa de Enlace**: Capa que agrupa protocolos de comunicación que permiten conectar físicamente a un dispositivo a la red.
  - _Ejemplos de Protocolos_: _Ethernet_, _Wi-Fi_, _ARP_, _NDP_, _OSPF_, etc.
- **Capa de Red o Internet**: Capa que agrupa protocolos de comunicación que se utilizan para transportar paquetes de información entre equipos conectados a la red.
  - _Ejemplos de protocolos_: _IPv4_, _IPv6_, _ICMP_, etc.
- **Capa de Transporte**: Capa que entrega servicios de comunicación entre dispositivos a aplicaciones
  - _Ejemplos de protocolos_: _TCP_, _UDP_, etc.
- **Capa de Aplicación**: Capa en la que se agrupan todas las aplicaciones que se ejecutan entre dispositivos.
  - _Ejemplos de protocolos_: _HTTP_, _DNS_, _IMAP_, _FTP_, etc.

La imagen siguiente (elaborada por `Cburnett` y subida a [Wikimedia Commons](https://en.wikipedia.org/wiki/Internet_protocol_suite#/media/File:UDP_encapsulation.svg)) muestra cómo cada capa "envuelve" los datos de las capas superiores, en el caso concreto de uso de protocolo de transporte _UDP_.

![Encapsulación en el caso del protocolo UDP](../UDP_encapsulation.svg)

## Interfaces de Red

Corresponden a dispositivos reales o virtuales por los cuales viajan paquetes de comunicación.

En Kali, pueden listar estos dispositivos con el comando `ip link show`. Este comando debería mostrarles algo parecido a esto:

```bash
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:a6:1f:86 brd ff:ff:ff:ff:ff:ff
```

- La interfaz `lo` corresponde a una _interfaz virtual_ denominada `loopback` y usada para enrutar paquetes a la misma máquina sin necesidad de otras interfaces.
- La interfaz `eth0` desde el punto de vista de Kali se comporta como una _interfaz real_, es decir, correspondería a una tarjeta de red independiente en el caso de un sistema operativo no emulado.

Cada una de las interfaces anteriores posee una _Dirección MAC_, un conjunto de 6 bytes único en cada subred utilizado para enrutar paquetes en la capa de enlace. Al mismo tiempo, cada interfaz bien configurada debiese poseer una _Dirección IP_, la que le permite enrutar paquetes en la capa de red.

## Wireshark

[Wireshark](https://www.wireshark.org/) es una herramienta de código abierto que permite capturar y analizar tráfico de protocolos de red. En esta parte del apunte veremos cómo utilizarla para interceptar paquetes del stack de internet y otros protocolos populares.

### Uso general de Wireshark

Wireshark se puede instalar con el gestor de paquetes de Kali Linux:

```bash
sudo apt install wireshark
```

Luego, podrán encontrar el ícono en el menú de aplicaciones. Para ejecutar Wireshark, se les solicitará la contraseña de superusuario, dado que es necesaria para poder monitorear las interfaces de red.

Al iniciar Wireshark, se encontrarán con esta vista:

![](../forensics-1.png)

En la lista del centro, se observan las distintas interfaces presentes en el computador, además de una especial, denominada `any`, la cual agrupa todos los resultados de las demás interfaces.

Si hacen click en una interfaz (por ejemplo, `eth0`), verán la siguiente pantalla.

![](../forensics-2.png)

En el número (1) encontrarán los distintos paquetes interceptados por Wireshark, mientras que en (2) verán el paquete disecado, capa por capa, y en (3) verán el contenido del paquete como _hexdump_. Métanse por ejemplo a `https://cc5325.xor.cl` mientras Wireshark está funcionando y luego vuelvan a Wireshark. Les aparecerá algo así:

![](../forensics-3.png)

En la imagen se alcanzan a ver 3 etapas de la consulta a la página web del curso:

- **Consultas DNS**, en color celeste, representan las llamadas al resolver DNS del computador para determinar la IP asociada al dominio cc5325.xor.cl.
- **Paquetes TCP**: En gris y morado, Se conectan con la IP indicada en el paso anterior, para inicializar una conexión con el servidor
- **Paquetes TLS**: En morado, corresponden a los paquetes usados para la transmisión de los contenidos de la página. No podemos ver su contenido en texto plano porque TLS es una conexión cifrada.

### Análisis de protocolos

A continuación veremos algunos ejemplos de uso básicos de Wireshark, los cuales consideran su inicialización, el uso de filtros de visualización y la exportación de archivos y datos.

#### Filtros básicos

Partamos revisando un caso básico de comunicación. Hablaremos con el servidor de la tarea 2. Para ello, hay que recordar que es necesario conectarse primero a la VPN del CEC y luego abrir la interfaz `any` en el menú inicial, de forma de ver mezclados paquetes de todas las interfaces (`eth0` y `tun0`, la segunda generada cuando se realiza la conexión OpenVPN.)

Luego, podemos intentar ejecutar el comando `nc server.cc5325.xor.cl 25102`, enviar un mensaje y recibir una respuesta. Ahora podemos revisar Wireshark para ver los paquetes enviados en este intercambio:

![](../forensics-2021-05-23-00-21-00.png)

Lo primero que notamos de la situación anterior es que se han enviado y recibido varios tipos de paquetes. para lo que nos puede servir aprender a usar los _filtros de visualización de Wireshark_ (Ctrl+/). A continuación mostramos algunos ejemplos.

- **Filtrar por puerto de origen/destino**: Para filtrar por puerto de origen o destino con un protocolo que usa `tcp` en la capa de transporte, se puede escribir en la barra de direcciones `tcp.port` seguido de un comparador (`>`, `==`, `<`) y luego del valor de puerto contra el cual se quiere comparar. Si se quiere filtrar solo por puerto de origen, usar el filtro `tcp.srcport` y si se quiere filtrar solo por puerto de destino, usar `tcp.dstport`. Análogamente existen filtros para protocolos que usen `udp`.
- **Filtrar por IP de origen/destino**: Para filtrar por IP de origen o destino se usa el filtro `ip.addr`. Para filtrar solo por IP de origen, se usa `ip.src` y para filtrar solo por IP de destino se usa `ip.dst`.

Es posible componer los filtros con operadores lógicos (`&& / and`, `|| / or`, `! / not`):

- **Ejemplo**: !(udp.port == 53) && ip.src == 127.0.0.1

Más información de los filtros se puede encontrar en [esta documentación](https://wiki.wireshark.org/DisplayFilters)

#### Revisar y exportar contenido

A continuación se muestra los mensajes enviados y recibidos en la terminal con `netcat`.

![](../forensics-2021-05-23-01-03-01.png)

De los mensajes anteriores, se puede ver esta captura de paquetes por Wireshark. Si nos fijamos en el tercer recuadro, notaremos que logramos interceptar el mensaje en texto plano enviado por el servidor a nuestra terminal.

![](../forensics-2021-05-23-01-04-07.png)

Lo anterior incluso sirve con protocolos más sofisticados, como HTTP. Para revisar esto, naveguemos en Firefox dentro de kali a la URL [http://info.cern.ch/](http://info.cern.ch/). Luego, filtremos por visualización paquetes tcp al puerto 80 y revisemos el contenido del mensaje. En la siguiente imágen podemos ver parte de la consulta HTTP de nuestra máquina virtual al servidor remoto:

![](../forensics-2021-05-23-01-26-42.png)

Las flechas al lado de la consulta (en la columna No.) muestran cómo los paquetes se relacionan entre sí. En específico, nos indican que el paquete 2459 es la respuesta de la consulta hecha en el paquete 2457 (los números en sus Wireshark definitivamente variarán, ya que los paquetes se enumeran desde que se lanza la herramienta). Los otros paquetes cubiertos por la línea vertical son mensajes de capas más bajas (TCP en este caso).

En la parte inferior del paquete 2459 se puede ver parte del HTML de la página cargada en texto plano.

![](../forensics-2021-05-23-01-28-20.png)

Si quisieramos extraer esta página (o el archivo PNG del paquete) podemos hacer click derecho en el payload del paquete (última fila de la vista del cuadro intermedio) y hacer click en _Export Packet Bytes_ (o usar el acceso directo de teclado _Ctrl+Shift+X_). Luego elegir una ubicación para el archivo. Si lo guardamos con la extensión correcta, podremos abrirlo sin problemas después.

![](../forensics-2021-05-23-01-36-33.png)

#### Guardar un archivo de captura

Podemos guardar todos los paquetes capturados en la sesión ejecutando `File -> Save As...`, lo que nos permitirá exportar un archivo con extensión `.pacpng`. Luego podremos abrir este archivo en Wireshark y seguir analizándolo, o incluso compartirlo.

#### Seguir un stream de datos

Si quieres tener en un solo archivo todo un flujo de comunicación (_stream_), puedes hacer click derecho en el _frame_, luego en _follow_ y luego en la capa que deseas seguir. Por ejemplo, lo siguiente sigue el flujo de obtener el `index` de la página web:

![](../forensics-2021-05-23-01-49-39.png)

#### HTTPS y protocolos cifrados

Al inicio de esta sección vimos que a veces los paquetes viajan cifrados entre cliente y servidor. Esto quiere decir que se necesita de una llave que permita descifrar los datos que llegan y se van. Esta llave la suele manejar el mismo navegador al momento de realizar la conexión. Sin embargo, es posible configurar algunos navegadores para que exporten la llave.

Cabe destacar que en los CTF de forensics que no requieren romper algún tipo de cifrado obsoleto usado para la comunicación, se les suele entregar la llave que usa el navegador para desencriptar y encriptar los datos enviados, la cual luego puede configurarse en Wireshark para ser usada en el análisis de los paquetes.

A continuación veremos tanto como iniciar nuestro navegador para que esta llave se exporte, como qué hay que hacer para configurar Wireshark para que utilice esta llave.

- **Iniciar el navegador con la capacidad de loguear en un archivo sus llaves TLS**. Últimamente Firefox tiene problemas para configurarse con este modo, por lo que les recomendamos instalar (`sudo apt install chromium`) y ejecutar Chromium con el siguiente comando:
  - `SSLKEYLOGFILE=~/key.log chromium`
- **Navegar a algún sitio con HTTPS**, como por ejemplo, [dcc.uchile.cl](https://dcc.uchile.cl)

- **Importar llaves en Wireshark**

Abrir Wireshark y luego ir a `Edit -> Preferences`. Verás este menú:

![](../forensics-2021-05-23-15-42-32.png)

En `Protocols -> TLS` ir a (Pre)-Master-Secret log filename y seleccionar el archivo que debiese estar en `/home/kali/key.log`.

![](../forensics-2021-05-23-15-44-14.png)

Ahora si vamos a la interfaz `any` y visitamos el sitio web del DCC, veremos que aparte de los paquetes TLS, sí aparecen paquetes de tipo HTTP, los cuales son completamente explorables.

![](../forensics-2021-05-23-15-47-18.png)

### Otros protocolos revisables con Wireshark

Como se puede ver en el menú "Protocols" de las preferencias, los protocolos soportados por Wireshark son muchos. A continuación mostraremos algunos.

- **USB**: Es posible generar archivos de captura de la comunicación realizada entre un dispositivo USB y el computador. Para esto, basta con seguir [este tutorial](https://gitlab.com/wireshark/wireshark/-/wikis/CaptureSetup/USB). Probablemente sea necesario también revisar la [documentación](https://gitlab.com/wireshark/wireshark/-/wikis/USB) del protocolo USB en general y del dispositivo que estamos revisando.
- **Bluetooth**: También es posible capturar mensajes Bluetooth entre nuestro computador y otro dispositivo usando [esta guía](https://gitlab.com/wireshark/wireshark/-/wikis/CaptureSetup/Bluetooth). Puede ser necesario revisar la [documentación](https://gitlab.com/wireshark/wireshark/-/wikis/Bluetooth) del protocolo Bluetooth.
