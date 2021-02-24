---
title : "Técnicas Básicas de Análisis Web"
description: "TODO"
lead: ""
date: 2020-10-06T08:48:45+00:00
lastmod: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "apps-web"
weight: 020
---

## Motivación

En este capítulo hablaremos de algunas de las técnicas más básicas utilizadas para en análisis web.
Para estas no se requiere ningún o casi ningún conocimiento sobre el funcionamiento o características del sitio,
y pueden ser aplicadas de manera casi inmediata. Usualmente se utiliza herramientas muy simples, que
requieren muy poca configuración para ser usadas. Desde el lado del servidor, suele ser bastante fácil detectar el uso de estas herramientas, por lo que
los sistemas relativamente bien monitoreados usualmente bloquean IPs con este comportamiento.

El objetivo de las herramientas que veremos ahora es obtener más información sobre el servicio web,
encontrando archivos, usuarios y otros recursos que pueden estar escondidos. Si tienen mucha suerte,
esto también puede resultar en la divulgación de información privada, sensible o crítica,
o incluso pueden ganar privilegios si logran encontrar contraseñas.

## Enumeración

La enumeración es un proceso en el cual se itera por una lista de valores (llamadas diccionarios), intentando
encontrar información nueva. Esto se puede aplicar a subdirectorios de un sitio web, subdominios,
nombres de usuario, nombres de parámetros, servicios ofrecidos, puertos abiertos, etc.
También se puede utilizar fuzzers, los cuales toman un input conocido y lo modifican de múltiples maneras
para encontrar otros inputs con comportamientos diferentes.

Este proceso funciona enviando las distintas peticiones al servidor y analizando sus respuestas. No se
suele encontrar muchas vulnerabilidades de esta forma, pero sí se logra recopilar información
y funcionalidades previamente no vistas.

Las herramientas comúnmente usadas en el área web son:
* [Gobuster](https://github.com/OJ/gobuster)
* [Dirsearch](https://github.com/maurosoria/dirsearch)
* [Dirbuster](https://github.com/KajanM/DirBuster)
* [Dirb](https://github.com/v0re/dirb)
* [Sublist3r](https://github.com/aboul3la/Sublist3r)
* [Wfuzz](https://github.com/xmendez/wfuzz)
* [Ffuf](https://github.com/ffuf/ffuf)

## Fuerza Bruta

Similar a la enumeración, pero en este caso se intenta pasar por todos o casi todos los valores posibles
de un parámetro, aunque en muchos casos también se utiliza diccionarios. Se diferencian principalmente
de manera conceptual, y en que la acción realizada usualmente tiene uno o unos pocos valores "correctos",
los cuales resultan en una respuesta diferente del servidor (por ejemplo, ingresar una contraseña correcta
tiene un resultado diferente al de ingresar una contraseña incorrecta).
Mediante la fuerza bruta se pueden encontrar contraseñas de usuarios, valores
aleatorizados, parámetros mágicos, secuencias específicas, etc.

Las herramientas usualmente utilizadas son:
* [Hydra](https://github.com/vanhauser-thc/thc-hydra)
* Varios módulos de [Metasploit](https://github.com/rapid7/metasploit-framework)
