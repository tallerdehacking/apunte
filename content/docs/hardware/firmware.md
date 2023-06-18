---
title : "Reversing de Firmware"
lead: ""
date: 2023-06-14T09:25:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "hardware"
weight: 020

---

El _firmware_ es el código básico que le permite al dispositivo saber cómo funcionar.
Le indica cómo encenderse, iniciar servicios, utilizar los sensores, comunicarse
y sus configuraciones principales. El _firmware_ puede tomar muchas formas diferentes;
puede ser código binario, ejecutables, o incluso un sistema operativo completo.

Este último es el caso para muchos dispotiviso IoT, como cámaras de seguridad,
impresoras, routers, y sensores de todo tipo. Como caso de estudio veremos el siguiente dispositivo:
[TP-Link Wireless N Router TL-WR841N V14.80](https://www.tp-link.com/us/home-networking/wifi-router/tl-wr841n/).
Pueden descargar el firmware desde su [página oficial](https://www.tp-link.com/us/support/download/tl-wr841n/#Firmware).

Para este caso usaremos la versión 14.8_220816, publicada en la fecha 2022-11-23.

![Firmware](../tp-link-firmware.png)

Al descargarlo vemos que es un archivo `.zip` con dos documentos PDF y un `.bin`.

![Contenidos ZIP](../zip-contents.png)

Analizamos el contenido del binario usando `binwalk` y encontramos múltiples secciones
interesantes.

* **U-Boot**: Es un _boot loader_ que empaqueta las instrucciones para iniciar el
kernel del sistema operativo.
* **LZMA**: Es un algoritmo de compresión. Contiene algunos datos utilizados por el dispositivo.
* **SquashFS**: Es el sistema de archivos de un sistema operativo, comprimidos en un solo archivo. 

![Binwalk](../binwalk.png)

Afortunadamente, `binwalk` es capaz de extraer estas secciones automáticamente:

```
binwalk -e TL-WR841Nv14_US_0.9.1_4.19_up_boot\[220816-rel43928\].bin
```

Obtenemos algunos documentos y directorios.

![Contenido Squashfs](../contents-squashfs.png)

Y en particular, el directorio `squashfs-root` es la raíz de un sistema de archivos Linux.

![Sistema de archivos Linux](../linux-fs.png)

Finalmente, encontramos el hash de la contraseña por defecto para el usuario admin contenida
en el archivo `squashfs-root/etc/passwd.bak`.

![Password](../password.png)

Almacenamos el hash en el archivo `hash.txt` y lo rompemos usando `hashcat`.
La contraseña resulta ser `1234`.

```
hashcat -a 0 -m 500 hash.txt /usr/share/wordlists/rockyou.txt
```

![Hashcat](../hashcat.png)

De esta forma se puede analizar diferentes componentes del firmware, para encontrar
secretos, configuraciones y funcionalidades del dispositivo. Dado que la gran mayoría
de los usuarios no cambia las configuraciones por defecto, es muy probable que
cualquier falla de seguridad encontrada al analizar el firmware, también se encuentre
en los dispositivos en uso. Adicionalmente, si existe una vulnerabilidad inherente
al _firmware_ (por ejemplo un _buffer overflow_), esta será explotable en todos los
dispositivos corriendo con dicho _firmware_.
