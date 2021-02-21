---
title : "Intro a Aplicaciones Web"
description: "TODO"
lead: ""
date: 2020-10-06T08:48:45+00:00
lastmod: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "apps-web"
weight: 010
---

# Motivación

Web es uno de los temas más amplios en las competencias de CTF.
Los challenges se basan principalmente en la explotación de vulnerabilidades reales en los sistemas,
pero también pueden incorporar elementos de otros temas también, como Stego, OSINT o PWN.
Para efectos de este curso nos centraremos en la detección y explotación de vulnerabilidades comunes,
mientras que la resolución de los challenges surgirá casi como un efecto secundario.

Ya que este tema hace un fuerte uso de vulnerabilidades reales, al practicar para este tipo de challenges
también están estudiando para hacer análisis de seguridad a sitios web de verdad. De hecho,
el penetration testing, o pentesting, de páginas web es el trabajo más solicitado a los especialistas en seguridad computacional.
Es más, algunas empresas buscan activamente a gente con habilidades en estos temas por medio de CTF,
para luego ofrecerles trabajo.

Similarmente a los otros temas que hemos visto en este curso, las flags de los challenges web pueden estar
en casi cualquier lado. Desde el código fuente HTML, pasando por parámetros retornados por el
servidor, y hasta pueden estar escondidas en una base de datos o en un archivo no visible desde internet.
Pero dentro de toda esta inmensidad de posibilidades, ustedes se deben guiar por las vulnerabilidades
y los recursos ganados al explotarlas.

# Análisis Básico de Aplicaciones Web

El análisis de aplicaciones web abarca temas muy amplios y se puede volver muy complejo, pero en su objetivo
fundamental es siempre el mismo: realizar acciones (ya sea leer, crear o modificar datos, ejecutar comandos,
u obtener privilegios diferentes) las cuales no son deseables por el dueño del sistema. Esto es, "hackear"
la página. Existen muchas técnicas, herramientas y procedimientos distintos que ayudan en este proceso,
pero en su forma más básica (similar al debugging de cualquier software),
esto se divide en análisis estático y análisis dinámico.

## Análisis Estático

Se refiere al análisis de elementos estáticos de un sitio web, como archivos HTML y JavaScript, código fuente,
restricciones de uso para ciertos campos (por ejemplo largo de la entrada, caracteres permitidos, etc).
Usualmente este es el primer paso para analizar un sitio web, con el cual se empieza a entender el funcionamiento
principal de la página, se encuentran las tecnologías utilizadas y de vez en cuando aparecen ciertos elementos
que no deberían estar visibles y que divulgan cierta información.

Este tipo de análisis es bastante simple y usualmente no se necesita más que un navegador. El más utilizado
en el área de seguridad es [FireFox](https://www.mozilla.org/en-US/firefox/new/), ya que se suele comportar
un poco mejor con las otras herramientas que se utiliza.

## Análisis Dinámico

El análisis dinámico incluye toda la revisión de requests hechas al servidor, junto a sus respuestas respectivas,
la generación de requests diferentes a los usualmente utilizados por el servicio, y en general a todo lo que
tenga que ver con interactuar con el servidor. Aquí es donde se encuentra la gran mayoría de las vulnerabilidades
y formas de explotar el servicio. La forma de realizar el análisis y sus resultados dependen fuertemente
de las tecnologías (lenguajes, frameworks, librerías, filtros, etc) usadas en el sitio web.

Para hacer esto, las herramientas más típicas son proxies. El más usado es [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload),
o [Burp Suite Professional](https://portswigger.net/burp/pro) si trabajan en una empresa o pueden costearlo.
Este no solo sirve de proxy, sino que además incluye algunas otras herramientas que ayudan a analizar consultas
e interactuar con el servidor. Durante este curso lo usaremos bastante, por lo que es recomendado instalarlo,
junto a algún plugin para redirigir las consultas, como por ejemplo [FoxyProxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/).

# OWASP

[The Open Web Application Security Project](https://owasp.org/) es una organización sin fines de lucro que intenta
mejorar la seguridad del software en general. Desarrollan diferentes proyectos para ayudar a
las personas a generar mejores sistemas y código. Estos comprenden guías de desarrollo y testeo,
definiciones de estándares y herramientas automatizadas, lo cual facilita el desarrollo de software
seguro y de calidad.

## Top 10 Web Application Security Risks

El [OWASP Top 10](https://owasp.org/www-project-top-ten/) es un proyecto que recopila los 10 riesgos de
seguridad más comunes en aplicaciones web. Estos riesgos usualmente se traducen en vulnerabilidades bajo ciertas
condiciones, por lo que es importante que al menos conozcan que existen y entiendan por qué surgen.
Estos riesgos son:
1. Injection
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Using Components With Known Vulnerabilities
10. Insufficient Logging & Monitoring

La mayoría de los nombres son bastante autodescriptivos, sin embargo si desean conocer estos riesgos
más en detalle, por favor visiten el proyecto de OWASP y lean su documentación.

## Web Security Testing Guide

La [Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) es una guía que intenta
estandarizar la forma de realizar pruebas de seguridad a una aplicación web. Es particularmente útil para
las personas que quieran seguir en esta área, ya que entra en harto detalle sobre cómo funciona cada ataque
y de qué forma se puede realizar.

## Otros Proyectos de OWASP

Otros proyectos de OWASP incluyen:

* [Dependency Track](https://owasp.org/www-project-dependency-track/): Una herramienta que analiza estáticamente
las dependencias de un proyecto y las compara con repositorios de software con vulnerabilidades conocidas,
  avisando si se utiliza alguno de estos.

* [Juice Shop](https://owasp.org/www-project-juice-shop/): Es un sitio web especialmente diseñado para ser vulnerable
a cada uno de los elementos en el OWASP Top 10. Es muy útil para practicar el pentesting.

* [Mobile Security Testing Guide](https://owasp.org/www-project-mobile-security-testing-guide/): Similar a la
Web Security Testing Guide, pero para aplicaciones móviles.

* [ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/): Es un set de reglas
genéricas de detección de ataques, compatibles con firewalls, Web Application Firewalls (WAFs) y otros filtros.

* [Software Assurance Maturity Model (SAMM)](https://owasp.org/www-project-samm/): Es un modelo de desarrollo
que ayuda a analizar y mejorar los ciclos de desarrollo seguro del software.

* [Security Knowledge Framework](https://owasp.org/www-project-security-knowledge-framework/): Base de datos de
checklists y buenas prácticas para proyectos para múltiples lenguajes de programación, que muestran cómo prevenir
  el acceso de hackers al sistema.

* [Zed Attack Proxy (ZAP)](https://owasp.org/www-project-zap/): Herramienta automatizada de análisis web dinámico.
Realiza una serie estandarizada de pruebas a aplicaciones web para encontrar vulnerabilidades comunes.


