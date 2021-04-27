---
title: "Optimus Prime"
description: "Writeup del problema 'Oprtimus Prime' de Hack The box'"
date: 2020-10-06T08:49:55+00:00
draft: false
menu:
  writeups:
    parent: "crypto"
images: []
---

## Desafío

En este desafío tenemos un servidor que nos da las siguientes opciones:

![pantallazo opciones servidor](../consolaprime.png)

De la 1 a la 3 no nos entregan información útil, pero la 4 nos da lo siguiente:

![información opción 4 servidor](../prime-opcion-4.png)

Un par llave, texto encriptado. Si se está usando RSA "de libro" no podemos hacer mucho 😢.
Al final de este archivo hay un código base que les puede servir para resolverlo

## Solución
Si tuviéramos algo como phi(n) podríamos desencriptarlo.

Lo primero que debemos notar es que si volvemos a mandar 4, el servidor nos responde con otra cosa. Como sabemos que el mensaje a encriptar es el mismo, lo único que ha cambiado es la llave.

Después de mucho probar cosas, probamos corriendo `miller_rabin` en la llave. Con eso tenemos nuestro primer paso: podemos intentar encontrar sus factores para obtener phi(n).

Como ya sabemos, encontrar los factores de un número grande es muy caro computacionalmente. Así que probamos otra cosa: ¿qué pasa si las llaves que nos manda el servidor tienen un factor en común?. Probamos con la función GCD, y nos entrega lo que buscamos. _Nota: esta parte es pura "suerte", y al final hay que estar probando distintas cosas hasta que nos damos cuenta de eso_

Con eso, encontramos un factor de la segunda llave. Luego, podemos ver que ese factor sí es primo usando `miller_rabin` de nuevo. Podemos definir entonces `p = GCD(key1, key2)` y `q = key2 // p`.

Después de eso, podemos calcular d usando `pow(e, -1, phi)`, y sacar la contraseña usando la desencriptación de RSA. El único dato que no tenemos para esto es `e`, pero lo sacamos probando valores comunes.

Finalmente, mandamos la contraseña desencriptada al servidor (sin haber cerrado el socket con el que recibimos la segunda llave), y obtenemos la flag.

## Anexo
### Código base
```python
#!/usr/bin/python3
import socketserver
from Crypto.Util.number import GCD
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA
import os
import secrets

import socket

# Acá colocamos los datos IP (o dominio) y puerto de la máquina con el challenge.
HOST, PORT = ("host", 1)

def receive_message(sock, message_length, endwith='\n'):
    """
    Recibe un mensaje de largo message_length del servidor, o hasta que el
    mensaje termina en endwith
    """
    received_message = ""
    while len(received_message) < message_length:
        if len(received_message) > 0 and received_message.endswith(endwith):
            break 
        received_part = sock.recv(message_length - len(received_message))
        received_message += received_part.decode("utf-8")
    return received_message


def receive_key_and_encrypted_pass(sock):
    # Implementar!
    pass


def miller_rabin(n, k):
    """
    Performs a Miller-Rabin primality test k times over n,
    Using the pseudo code from Wikipedia.
    We need this function to check if our big random numbers are primes or not.
    (A classic sieve is too slow for our magnitudes (~2048 bits)
    :param n: number to check
    :param k: number of times to make the check
    :return true if number is probably prime, false otherwise:
    """
    if n == 1:
        return False
    elif n % 2 == 0:
        return n == 2  # return true only if n is pair and 2, if it is pair and not 2 return false
    elif n == 3 or n == 5:
        return True
    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d >>= 1
    # now n = 2^r * d
    for i in range(k):
        a = secrets.randbelow(n - 5) + 2  # a \in [2, n-2]
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        key1, password1 = receive_key_and_encrypted_pass(s)
        s.close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        key2, password2 = receive_key_and_encrypted_pass(s)

```