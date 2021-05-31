---
title: "Intro al Pwning"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "pwning"
weight: 010
---

_Pwn_ (Suele pronunciarse como la palabra española "pon") es una palabra de la jerga [leetspeak](https://en.wikipedia.org/wiki/Leet), nacida de una derivación del término _Own_ (Poseer en inglés), y se refiere en este contexto a la capacidad de unx hacker de controlar una máquina que no es suya a partir del aprovechamiento de vulnerabilidades en ella.

En general, los desafíos de _Pwning_ son bastante variados y pueden tener partes de otras categorías ya vistas (reversing, web, crypto, etc), pero se parecen en que el resultado final consiste en adquirir permisos de superusuario en una máquina. En esta unidad, nos enfocaremos en desafíos de pwning relacionados con escalar privilegios en Linux y con explotar vulnerabilidades básicas en algunos servicios.

La unidad entonces se dividirá en dos partes

**Escalamiento de privilegios básico**: Partiremos explicando algunas técnicas de escalamiento de privilegios a partir de programas ejecutables en una máquina Linux, contando solamente con usuarios con privilegios limitados.

**Buffer Overflow**: Conseguir acceso de superusuario a partir de la explotación de una vulnerabilidad conocida como "buffer overflow" en entradas de programas y servicios con privilegios ejecutados por máquinas remotas.

No tocaremos vulnerabilidades de control de flujo avanzadas, pero intentaremos dejar bibliografía para que puedan investigar por su cuenta.
