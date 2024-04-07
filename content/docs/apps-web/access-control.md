---
title : "Broken Access Control"
lead: ""
date: 2024-04-03T22:45:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "apps-web"
weight: 307
---

El control de acceso es una política aplicada a los usuarios, 
de manera que no puedan actuar fuera de sus permisos asignados. 
Las fallas en estas políticas suelen conllevar a la pérdida de 
confidencialidad, modificación o destrucción de recursos, o la 
ejecución de procesos no autorizados. 

A continuación veremos algunos ejemplos de pérdida de control de acceso, 
sin embargo, esta clase de vulnerabilidades no se limita únicamente
a estos. 

## Principio del Privilegio Mínimo

El principio del privilegio mínimo (PoLP: Principle of least privilege) 
se refiere a la práctica de asignar los permisos estrictamente necesarios
para el funcionamiento del sistema, y nada más. Aplica a usuarios, procesos, 
archivos, y cualquier otro tipo de entidad a la cual se le pueda restringir 
su capacidad de acción mediante permisos o privilegios. 

Un sistema que no siga el PoLP abre la posibilidad a accesos no permitidos, 
lo que podría resultar en robo, alteración o destrucción de información, 
movimientos laterales o escalación de privilegios. En términos más concretos, 
se está permitiendo el acceso a recursos que no se debería tener acceso. 

Muchas veces los desarrolladores piensan que implementando medidas de control
de acceso en el frontend, están evitando este tipo de situaciones: "Si el botón
no aparece en las opciones, el usuario no puede realizar esta acción". Esto, sin 
embargo, no es correcto. Un atacante puede forzar el envío de ciertas peticiones
HTTP y gatillar estas funcionalidades restringidas, evadiendo el intento de 
control de acceso. 

## Insecure Direct Object Reference

La vulnerabilidad conocida como Insecure Direct Object Reference (IDOR) 
es un caso particular de la ausencia de control de acceso, y ocurre 
en situaciones donde se acceda a un objeto por medio de un identificador
único. Esto es muy prevalente en APIs, pero también ocurre en otras instancias. 

Un ejemplo de esto es obtener el perfil de otro usuario. Supongamos que 
para ver nuestro perfil, se envía una petición GET hacia `/profile?id=5325`.
Ahora, si los controles de acceso no están bien implementados, podríamos
obtener el perfil de otro usuario si modificamos la URL `/profile?id=1234`.

> TIP: 
> Casi siempre el primer usuario creado en cualquier sistema es el usuario 
> administrador. Esto significa que al buscar `/profile?id=0` estamos
> potencialmente obteniendo el perfil del administrador. 

Veamos cómo podemos aplicar esto en el [Juice Shop](https://owasp.org/www-project-juice-shop/)
de OWASP. Para este caso, el IDOR existe en la funcionalidad 
del carrito de compras. Primero debemos crear una cuenta e iniciar sesión:

![Juice Shop Login](../juiceshop-login.png)

Luego agregamos algún producto cualquiera al carrito:

![Juice Shop Add to cart](../juiceshop-add-to-cart.png)

Esto gatilla una petición para obtener el contenido de nuestro carrito:

![Juice Shop My basket](../juiceshop-my-basket.png)

Si modificamos el identificador en la URL, podemos obtener el carrito de otro usuario:

![Juice Shop IDOR](../juiceshop-idor.png)

## Forced Browsing

La vulnerabilidad de Forced Browsing es similar a la falla en el 
Principio del Privilegio Mínimo. En este caso, se permite a los usuairos
navegar a vistas restringidas, cambiando la URL en la que se encuentran. 

Por ejemplo, si podemos acceder al panel de administración simplemente
accediendo a la URL `/admin`, estamos en presencia de un Forced Browsing. 
Para esto, muchas veces se requiere tener algún tipo de sesión activa, 
sin importar los privilegios del usuario. 

Otro ejemplo de esto podría ser si tenemos acceso únicamente a un 
listado de usuarios en `/list-users`, y lo modificamos a 
`/edit-users`. Luego, tendríamos la capacidad de editar usuarios. 

Para encontrar este tipo de vulnerabilidades se puede buscar referencias 
a las URLs restringidas en los archivos JavaScript del sitio web, 
o enumerar directorios y archivos con alguna herramienta. 
La enumeración debe ser realizada utilizando una sesión de usuario
de ser posible. 

```bash
dirsearch -u 'http://localhost/' --cookie 'SESSION=cookie'
```

Probando esto en Juice Shop obtenemos lo siguiente:

```bash
dirsearch -u http://localhost:3000/ --cookie 'language=en; welcomebanner_status=dismiss; continueCode=MN53Kp8wVOl4WEgvQBKz1DoX7e2x0eBPAYbr9yjp3qPm6MZLnak5NJRRy6zv; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNj
ZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0QHRlc3QudGVzdCIsInBhc3N3b3JkIjoiYWUyYjFmY2E1MTU5NDllNWQ1NGZiMjJiOGVkOTU1NzUiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoidW5kZWZpbmVkIiwicHJvZml
sZUltYWdlIjoiL2Fzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdC5zdmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjQtMDQtMDcgMTU6MTY6NDEuNjU3ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjQtMDQtMDcgMTU6Mjg6NTUuNTI2ICswMDowMC
IsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTcxMjUwMzg0MH0.EMSR5vZI983opfLuRmaAEfaJ3riPnEUJfCbz0tKM2nvPu3piD_ggpw0LKKdiU251Db1FqtubhBEkDWvaoMnYtuGF1TO-UdssJEHyJFAdpuO-QimIt7-0qg3mF09SAUfMMSpOsN1czSJm3dehH6bZiRFEUsYufxnrmM4JoWYMGHU'
```

![Juice Shop dirsearch](../juiceshop-dirsearch.png)

Ingresamos a `http://localhost:3000/ftp` y encontramos el siguiente contenido:

![Juice Shop FTP](../juiceshop-ftp.png)


