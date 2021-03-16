---
title : "Common Vulnerabilities and Exposures"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "apps-web"
weight: 070
---

Muchas veces ustedes se encontrarán con sistemas (web u otro tipo) que utilizan software con vulnerabilidades
conocidas (punto 9 del OWASP Top 10). Estas vulnerabilidades se catalogan como _Common Vulnerabilities and
Exposures_ (CVE), el cual es un sistema que intenta proveer información y documentación sobre
vulnerabilidades conocidas públicamente.

## Herramientas

La herramienta más conocida y utilizada para la explotación de CVEs es [Metasploit](https://github.com/rapid7/metasploit-framework),
el cual es un repositorio de vulnerabilidades parametrizadas, para facilitar su explotación.
Además está [searchsploit](https://www.exploit-db.com/searchsploit), que es un repositorio con descripciones
y pruebas de concepto para algunos CVE que no aparecen en Metasploit.

Sin embargo no todos los CVEs están en esas herramientas, y tendrán que buscarlos en internet.
Algunos sitios útiles son:
* https://www.exploit-db.com/
* https://vuldb.com/
* https://medium.com/
* https://github.com/

En estos podrán encontrar códigos, pruebas de concepto, y guías paso a paso sobre cómo funcionan algunas
vulnerabilidades.

## Ejemplo

Para iniciar Metasploit deben correr el siguiente comando como `root`:

    msfdb run

Luego pueden buscar dentro del repositorio de vulnerabilidades por palabras clave `search <keyword>`:

![Metasploit Search](../metasploit-search.png)

Finalmente, para elegir un exploit, pueden ejecutar `use <num>` con el número del exploit en la lista retornada
de la búsqueda.

Recuerden que **las vulnerabilidades varían entre versiones de cada software**, por lo que no necesariamente
podrán explotarlas siempre.

Pueden encontrar un tutorial bastante completo de Metasploit [aquí](https://www.tutorialspoint.com/metasploit/index.htm).

Para buscar exploits en searchsploit, simplemente usar el comando `searchsploit <keyword>`:

![Searchsploit Searching](../searchsploit-searching.png)

Esto les retornará una lista de exploits con un nombre y una ruta al archivo con la descripción o prueba de concepto.
Si el archivo es `.rb` significa que existe un módulo de Metasploit implementado. Sino, tendrán que leer la
descripción e llevar a cabo la explotación de manera manual.

Los archivos están nombrados con un código numérico que los identifica. Si quieren ver el archivo,
pueden imprimir la ruta completa a este usando `searchsploit -p <code>`:

![Searchsploit Path](../searchsploit-path.png)
