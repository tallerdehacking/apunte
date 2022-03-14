---
title: "Máquina cifradora"
description: ""
date: 2020-10-06T08:49:55+00:00
draft: false
menu:
  writeups:
    parent: "stego"
images: []
---

Un amigo creó una máquina para cifrar mensajes. La usa para todo: cifrar textos secretos, usuarios y contraseñas personales, entre otros. Está tan confiado en que su algoritmo es altamente irrompible, que me envió su código fuente a modo de prueba.

```python
# !/usr/bin/python3
# !/usr/bin/python3

import base64
import codecs

# TODO: Delete this
# 5447456759327868646q55676332566n636q56305953426p63794244517n557n4q6n556r657964304q46426662444r324q327866557n4r6n636n4q334n33306r


class Message:
    def __init__(self, message):
        self.message = message

    def encode(self):
        message_bytes = self.message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        hex_message = base64_bytes.hex()
        rot13_message = codecs.encode(hex_message, 'rot_13')
        return rot13_message


def main():
    msg = input('Ingresa el mensaje secreto que quieres cifrar: ')
    message = Message(msg)
    print("Mensaje cifrado: ", message.encode())


if __name__ == '__main__':
    main()

```
