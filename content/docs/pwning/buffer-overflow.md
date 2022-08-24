---
title: "Buffer Overflow"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "pwning"
weight: 70040
---

### Buffer Overflow

Los ataques de secuestro de control de flujo consisten en aprovechar la entrada de datos de un programa para modificar las instrucciones a ejecutar por este, a partir del aprovechamiento de características propias de la arquitectura del sistema. En este apunte nos enfocaremos en un problema de seguridad denominado __Buffer Overflow__, el cual sobreescribe parte de la sección de memoria encargada de definir a qué líneas de código ejecutar.

Partiremos este capítulo explicando cómo funciona el manejo de memoria en sistemas con arquitectura x86, para luego hablar del ataque en específico. Finalizaremos con un pequeño ejemplo en código de cómo ejecutar un Buffer Overflow en un programa sin mecanismos de defensa.

### Instrucciones y registros en ASM

Como ya se vio en el capítulo de Reversing, el código que escribimos al programar en un lenguaje compilado es transformado en un código equivalente en funcionalidad pero mucho más simple de interpretar, denominado _Assembler_ (ASM). Este código corre con varias restricciones que no aplican en lenguajes de programación de más alto nivel:

* Las variables utilizables de forma directa se llaman **registros** y son limitadas en número y capacidad. Dependiendo de la arquitectura y del tipo de procesador, un registro puede guardar entre 8 y 256 bits. Los registros más importantes para conocer son: 
  - `eax`, `ebx`, `ecx`, `edx`: Registros de 32 bits utilizados de forma general, por ejemplo, para almacenar argumentos de una función. Si se les quita la `e` que llevan de prefijo, representan registros de 16 bits, y si se les cambia la `E` por una `r`.
  - `ebp`, `esp`, `edi`, `esi`, `eip`: Punteros, es decir, apuntan direcciones de memoria RAM en las cuales se encuentran datos a utilizar. La utilidad específica de algunos de ellos se explicará más adelante.
  - Operaciones `add`, `sub`, `mul`, `div`, `and`, `xor`: Sirven para operar entre 2 registros o constantes. El valor se guarda en un tercer registro definido en la misma instrucción.
  - Operaciones de pila `push` y `pop`: permiten sacar y agregar datos de una **pila**, la cual se definirá en la siguiente sección
  - Operaciones de control de flujo `cmp`, `je`, `jne`, `jg`, `jl`: Permiten condicionar la ejecución de código según un resultado de comparación previo (con `cmp`). También permiten implementar **loops**.
  - `flags` es un [registro especial](https://en.wikipedia.org/wiki/FLAGS_register) donde se guarda información sobre el estado del procesador. Algunas de las cosas que se guardan en él son:
    - `OF` o _Overflow Flag_, muestra si la última operación aritmética hizo overflow (hay reserva)
    - `PF` o _Parity Flag_, indica si el número de bits en valor 1 de la última operación binaria realizada es par o impar.
    - `ZF` o _Zero Flag_, indica que un resultado aritmético previo tenía valor 0.
    - `SF` o _Sign Flag_, indica el signo de la última operación aritmética
    - `CF` o _Carry Flag_, es usada para guardar una reserva en una operación aritmética, de forma de poder hacer operaciones con números más grandes que el tamaño de los registros.
### Punteros

A continuación mencionamos la utilidad de algunos punteros importantes:

 - `ebp` y `esp` marcan el inicio y el tope de la pila, respectivamente.
 - `edi` y `esi` se suelen usar para operaciones de copia de Strings
 - `eip`: o _instruction pointer_, apunta a la dirección de memoria en la cual se ubica la instrucción que se está ejecutando en ese momento.

### Manejo de Memoria

![Manejo de Memoria](../2021-06-17-00-17-38.png)

La imagen superior muestra cómo se ordena la memoria en un sistema x86. La imagen muestra las direcciones de memoria partiendo abajo y creciendo hacia arriba. Estas tienen un tamaño de 32 bits (4 bytes) y se acceden de 4 en 4 bytes.

Existen 6 bloques importantes en la memoria completa:

 - **Stack (Pila)** Acá se almacenan las variables locales de los programas. Veremos más adelante que cada vez que se llama a una nueva función, se agrega un _frame_ al stack. Un _frame_ equivale al ambiente local inmediato de variables locales de una función. Como se ve en la imagen, **El Stack crece hacia abajo** (direcciones de memoria decrecientes).
 - **Espacio Libre**: Entre el _stack_ y el _heap_ hay memoria libre. El crecimiento de ambos disminuye la cantidad de memoria libre disponible.
 - **Heap**: Espacio que maneja la memoria dinámica, es decir, en el caso de C, las variables declaradas con `malloc`, además de algunas funciones.
 - **BSS**: Memoria variable reservada antes de ejecutar el _main_ de un programa en C.
 - **Data**: Constantes.
 - **Text**: Instrucciones en ASM a ejecutar.

### El programa en memoria y su ejecución

En el bloque `Data` se ubica una copia de las instrucciones que componen el programa que se está ejecutando. Debido a lo anterior, este bloque suele ser _de solo lectura_. Para saber en qué instrucción se está en cada momento del programa, se almacena en `eip` el valor de la instrucción actual, el cual es incrementado en una posición cada vez que se finaliza de ejecutar una instrucción, excepto en casos en los que se ejecuta una instrucción `jmp`

Las instrucciones `cmp` y `test` actualiza

Las instrucciones `jmp` ejecutan un salto incondicional hacia una nueva dirección de memoria indicada en la misma instrucción. También existen _jump condicionales_, los cuales se ejecutan según el estado de flags del registro `flags`. [Acá](http://unixwiz.net/techtips/x86-jumps.html) se pueden ver los tipos de saltos.

### La Pila (_Stack_)

Como se mencionó anteriormente, la pila es el lugar en el que se guardan las variables locales de las funciones. Cada vez que entramos a una función, creamos un nuevo _frame_, el cual se inicializa como una pila vacía, en el cual colocamos las nuevas variables locales a crearse. Al momento de salir del frame, este se descarta, activándose nuevamente el frame inmediatamente anterior.

Al entrar a un nuevo frame, se guarda la dirección de memoria actual dentro de la función (`EIP`) en la misma pila, y luego este valor se llena con el de la función anidada. De esta forma, al salir de la función anidada, se sabrá como volver a la función anterior.

¿Cómo sabemos donde parte y donde termina la pila? Usamos los punteros `esp` y `ebp` para guardar estos datos. `ebp` registra la dirección de memoria en la cual parte el frame actual, mientras `esp` guarda la dirección de memoria siguiente a la última utilizada. Cuando se crea un frame nuevo, ambos valores se guardan en la pila y se setean al valor siguiente al último de la pila, emulando de este modo una pila vacía, ya que base y tope son la misma posición.

El siguiente conjunto de imágenes muestra cómo se opera en la pila y cómo se crean frames.

![](../2021-06-18-14-05-47.png)

![](../2021-06-18-14-06-41.png)

![](../2021-06-18-14-07-38.png)

Para eliminar un frame, se siguen los pasos inversos de la segunda imagen, es decir, se cargan los valores de más arriba de la pila como `esp`, `ebp` y `eip`.

### Shellcode

![](../2021-06-18-11-56-26.png)

¿Cómo se guarda el código que ejecutamos en `Data`? Al igual que cualquier dato del computador: usando `0s` y `1s`. Esto quiere decir que una variable con la forma y valor adecuado podría perfectamente ser interpretada como un programa si logramos que `EIP` apunte a la zona de memoria en que se encuentra guardada.

La representación en texto de un código ejecutable es conocida como `shellcode` cuando ésta permite levantar una `shell` luego de ser ejecutada.

Es posible encontrar un listado de shellcodes clasificados por OS y arquitectura de procesador en [este enlace](https://www.exploit-db.com/shellcodes) o [acá](http://shell-storm.org/shellcode/). También es posible crear shellcodes propios usando herramientas especiales o incluso a mano, como muestra [este tutorial](https://www.exploit-db.com/docs/english/13610-building-your-own-ud-shellcodes-part-1.pdf).

### El Ataque

Un ataque de Buffer Overflow se aprovecha de las nulas protecciones que algunos lenguajes de bajo nivel poseen sobre el acceso a memoria. Para ejemplificarlo, contaremos con el siguiente programa:

```c++
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("usage: %s name", argv[0]);
        exit(1);
    }
    char password = 'a';
    char  nombre[4];
    strcpy(nombre, argv[1]);
    printf("hola %s. Veremos si tienes acceso...\n", nombre);
    if (password == '#') {
        printf("Acceso otorgado! (password=%c)\n", password);
    } else {
        printf("Acceso denegado (password=%c)\n", password);
    }
    exit(0);
}
```

Las variables `password` y `nombre` se almacenan  en la pila de forma consecutiva. El espacio morado corresponde a cada byte en la pila de la variable `nombre`, y el espacio verde al único `char` de la variable `password`. Si guardamos "Ana" en `nombre`, el stack quedaría así:

![](../2021-06-18-15-15-29.png)

El `\0` final corresponde al byte nulo, usado para marcar el fin de una cadena de texto.

En cambio, si entregásemos el valor `Dani#` como `nombre`, el char de `password` se vería sobreescrito por el `#`, lo que nos dejaría entrar a la branch _Acceso otorgado!_.

![](../2021-06-18-22-13-56.png)

Esta misma estrategia de overflow en variables se puede usar para sobreescribir más allá de las variables locales:

Supongamos que estamos en una función con una variable local `nombre`. Más allá de esta variable encontraremos en la pila dos valores: `ret` (Dirección de retorno del `EIP` al finalizar la función) y `EBP`  (puntero a la base de la pila del frame inferior). Si agrandamos `nombre` lo suficiente, podremos sobreescribir `ret` con un valor a nuestra elección, el cual podría apuntar a una dirección de memoria en la que sabemos que hay código útil.

![](../2021-06-18-22-34-46.png)

La mejor referencia para entender paso a paso un Buffer Overflow la pueden encontrar en el artículo [Smashing the Stack for Fun and Profit](./smash-stacking.pdf) del colectivo Hacker _Aleph One_.
)

### Limitaciones:

Si bien lo anterior fue un problema sumamente grabe hace varios años, hoy en día existen una serie de mitigaciones en distintos niveles para evitar este tipo de comportamientos anómalos, acá mencionamos algunas:

* **A nivel de sist. Operativo**: Mitigaciones que dependen del sist. operativo usado para ejecutar el programa. Hoy en día todas se encuentran activas por defecto, salvo para la ejecución de programas antiguos que no las soportan.
 * **Write XOR Execute**: Característica que limita el uso de la memoria de un proeso para que ésta sea escribible O ejecutable, pero no ambas a la vez.
 * **ASLR**: Direcciones de memoria de una aplicación se aleatorizan en cada ejecución, con lo que se dificulta la posibilidad de saltar a un espacio específico.
 * **DEP**: Marcar algunas páginas de memoria como explícitamente no ejecutables.
* **A nivel de compilación**: Estas mitigaciones son flags del compilador que dificultan la explotación de buffer overflows.
 * **Stack Canaries**: Valores aleatorios en la pila que se colocan al entrar a un frame y luego se revisan al salir de él, de esta forma, se dificulta la modificación del stack a través de overflows, ya que es necesario adivinar el valor original del canario colocado.

 ### Uso en CTFs

Por temas de tiempo y de alcance, no contaremos en esta iteración del curso con material especial para preparar payloads en CTFs. Sin embargo, veremos en la clase en vivo el siguiente tutorial elaborado por [padragnix](https://padraignix.github.io/reverse-engineering/2019/09/28/buffer-overflow-practical-case-study). El link incluye harto material relacionado e incluso una presentación de PowerPoint para revisar.
