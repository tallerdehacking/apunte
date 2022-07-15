---
title : "Introducción al Análisis Forense"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "forense"
weight: 50010

---

El término "Análisis Forense" corresponde en grandes rasgos al trabajo de recolectar y analizar evidencia científica para el uso en una investigación criminal. El área de la ciberseguridad emplea este término para definir el conjunto de técnicas computacionales que permiten obtener información importante sobre dispositivos a partir del análisis de registros presentes en los sistemas analizados.

En términos concretos, algunas actividades relacionadas con el análisis forense computacional pueden ser:

* Revisión de _logs_ de programas o sistemas computacionales para determinar acciones realizadas o archivos exifiltrados luego de una intrusión a un sistema.
* Recuperación de archivos e información desde memoria RAM o almacenamiento secundario en máquinas reales o virtuales, ya sea a partir de archivos temporales, sistemas de versionamiento o de datos presentes de forma física en el dispositivo debido a una mala eliminación.

En el caso de competencias de tipo _Capture the Flag_, los desafíos de categoría forense utilizan técnicas inspiradas en el análisis forense computacional, siendo las _flag_ la información escondida en un archivo, comunicación o dispositivo.

En esta unidad del curso veremos algunos casos específicos de problemas de análisis forense. La idea es que puedan desarrollar la intuición inicial para adentrarse por su cuenta a problemas más complejos o relacionados con programas y dispositivos distintos a los vistos en el curso. En específico, veremos las siguientes categorías:

* **Comandos de consola en Linux útiles para análisis forense**: Esta sección enumerará algunos comandos de consola que les pueden ser útiles para CTFs con preguntas de análisis forense.
* **Análisis forense sobre Logs de sistemas y programas**: En esta sección se mostrarán las ubicaciones de los logs de algunos sistemas y programas de común uso.
* **Análisis forense para recuperar información eliminada**: En esta sección veremos técnicas y herramientas para recuperar archivos eliminados de un computador.
* **Análisis forense en versionado de archivos**: Esta sección explicará de forma breve el funcionamiento de algunos sistemas de versionamiento de archivos, y revisaremos herramientas que nos permitirán recuperar datos borrados en versiones más recientes.
* **Análisis forense sobre protocolos de comunicación**: En esta sección se revisará la herramienta `Wireshark`, la cual nos permite realizar análisis forense sobre logs de protocoles de comunicación conocidos. En específico, en este curso veremos protocolos de capa de red, transporte y aplicación del modelo de Internet y el protocolo USB.
