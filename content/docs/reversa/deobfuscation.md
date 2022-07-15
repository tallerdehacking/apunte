---
title : "Deobfuscación"
lead: ""
date: 2020-10-06T08:48:45+00:00
draft: false
images: []
menu:
  docs:
    parent: "reversa"
weight: 60030
---

La deobfuscación de ejecutables es similar a la deobfuscación de JavaScript que vimos en los capítulos de
esteganografía y aplicaciones web. La diferencia siendo que el código ahora puede estar compilado,
y por lo tanto las operaciones utilizadas para obfuscar la funcionalidad podrían estar a nivel de microcódigo.

Este tipo de obfuscación no hace más seguras las aplicaciones, ya que con suficiente trabajo siempre pueden
ser deobfuscadas, sino que intenta dificultar la lectura y entendimiento de estas a personas que no tengan
acceso al código fuente. Esto finalmente retrasa el hallazgo de diferentes tipos de vulnerabilidades, ya que
impone un trabajo previo a la investigación.

La obfuscación suele usarse también para ocultar _malware_ y evitar que sea detectado por sistemas de antivirus.
Estos funcionan mayoritariamente por la detección de firmas (_signatures_) de virus y malware conocidos, que
intentan identificarlos usando su ejecutable o comandos utilizados. La obfuscación puede cambiar la firma de un
ejecutable, y por lo tanto evadir la detección del antivirus.

## Obfuscación Básica

La obfuscación más básica, la cual solo es efectiva si el código original ya es relativamente complejo y extenso,
es modificar los nombres de variables, funciones y clases por caracteres aleatorios, al igual que quitar
todo tipo de comentarios e información extra que pueda ayudar a alguien a comprender su significado.
Luego, el código resultante no entrega ningún tipo de contexto sobre su funcionamiento, y este debe ser
analizado cuidadosamente para entenderlo.

Como ejemplo, tenemos este simple código en PHP que calcula la raíz cuadrada de un número usando el método de Newton.
A pesar de ser un código muy breve y sin mucha complejidad, esta obfuscación ya impone algo de esfuerzo para
entenderlo.

```php
function a0($f1,$c2){
  $w3=$f1;
  for($r4=0;$r4<$c2;$r4++){
    $w3=0.5*($w3+($f1/$w3));
  }
  return $w3;
}
$f1=$b5[1];
$c2=$b5[2];
$w3=a0($f1,$c2);
echo("$w3\n");
```

## Eval

Otra forma simple de obfuscación, utilizada mayoritariamente en lenguajes interpretados
(Python, PHP, JavaScript, etc) con la capacidad de evaluar código en tiempo de ejecución
(también es posible para lenguajes compilados como C/C++, Java o VBA, pero suele ser algo más complejo),
es el uso de codificación, compresión y encriptación (en cualquier orden y no necesariamente todos al mismo tiempo).
Es decir, se toma el payload, o código que se quiera obfuscar,
se codifica, comprime y encripta, y se almacena como un string o una constante en el código. Luego, al momento de
ejecutarlo, se debe desencriptar, descomprimir y decodificar, para finalmente evaluarlo (usando una función como
_eval_ o _exec_) en tiempo de ejecución.

Como ejemplo tenemos este pequeño código en Python. Pueden intentar decodificar ustedes mismos el payload.

```python
from base64 import b64decode
from zlib import decompress

payload = 'eJw1yzEKwkAQBdCr/ExlQPYC4gFsbNLaaHZwPyQza2YEc3ttbB+8vtHyIFd/eN2hn65zBrIppn43RsPFXm8Gk26DHNXqWW6bjKf+n4nqptg1SymYfNVstCcYiOSyYGXEDwYZv35UJm0='
decoded = b64decode(payload)
decompressed = decompress(decoded)

exec(decompressed)
```

Por sí solos estos métodos no son muy efectivos en contra de un humano (aunque sí contra muchos antivirus),
pues es muy evidente en dónde se está escondiendo el payload y cómo decodificarlo.

Para utilizar esta técnica con lenguajes compilados hay 2 opciones. La primera es pedirle al compilador que compile
el código decodificado y luego ejecutar el archivo resultante. El problema es que muchas veces la llamada al
compilador marca al programa como posible malware y este se bloquea.

La otra opción es tener el microcódigo compilado directamente almacenado en el código como payload. Luego, solo
se necesita crear un archivo con este contenido o cambiar el contenido de memoria de un proceso por el
microcódigo.

## String Splitting

El _string splitting_, o separación de strings, es un método utilizado para esconder constantes de tipo string
(como contraseñas, llaves privadas, URLs, mensajes, etc) en diversas partes.
Luego, todas estas partes se mezclan de cierta forma en particular para producir la variable original.
Las operaciones comúnmente utilizadas para esto son la concatenación, casting,
codificación en distintos estándares de texto, substrings, entre otros.

Por ejemplo, este código JavaScript esconde una contraseña obfuscada usando string splitting.
Notar que no todas las secciones se utilizan para construir la contraseña.

```javascript
var _0xfb5e=[
  '\x31\x33\x32\x30\x33\x35\x78\x6b\x4b\x76\x44\x62',
  '\x38\x4b\x6e\x7a\x6b\x74\x6c',
  '\x31\x30\x30\x30\x38\x45\x79\x6b\x4d\x68\x69',
  '\x24\x77\x30\x72',
  '\x31\x38\x38\x32\x33\x34\x6e\x6b\x73\x41\x55\x6a',
  '\x31\x30\x33\x36\x39\x35\x6f\x67\x54\x6e\x6f\x4a',
  '\x33\x63\x72\x65',
  '\x70\x33\x72\x53',
  '\x36\x36\x36\x36\x54\x6e\x52\x54\x6a\x73',
  '\x74\x50\x34\x73',
  '\x32\x37\x30\x38\x36\x38\x47\x61\x4b\x61\x50\x5a',
  '\x35\x38\x6d\x77\x67\x68\x6e\x50',
  '\x32\x39\x35\x33\x37\x79\x54\x62\x62\x42\x58',
  '\x4d\x79\x24\x75'
];
var _0x3683a0=_0x45f1;
function _0x45f1(_0x2320c9,_0xd2858e){
    _0x2320c9=_0x2320c9-0x10c;
    var _0xfb5e0e=_0xfb5e[_0x2320c9];
    return _0xfb5e0e;
}(
    function(_0x165719,_0x10ce39){
        var _0x2163ea=_0x45f1;
        while(true){
            try{
                var _0x26183c=parseInt(_0x2163ea(0x118))+-parseInt(_0x2163ea(0x10c))*parseInt(_0x2163ea(0x10f))+-parseInt(_0x2163ea(0x113))+-parseInt(_0x2163ea(0x10e))+-parseInt(_0x2163ea(0x112))+parseInt(_0x2163ea(0x116))+-parseInt(_0x2163ea(0x119))*-parseInt(_0x2163ea(0x110));
                if(_0x26183c===_0x10ce39) break;
                else _0x165719['push'](_0x165719['shift']());
            }catch(_0x3d8331){
                _0x165719['push'](_0x165719['shift']());
            }
        }
    }(_0xfb5e,0x3046a)
);
var password=_0x3683a0(0x10d)+_0x3683a0(0x115)+_0x3683a0(0x114)+_0x3683a0(0x117)+_0x3683a0(0x111)+'\x64';
```

A diferencia de la técnica anterior, es muy difícil para una persona saber qué es lo que está pasando y cómo se
construye la variable.

## Dead Branches

Otra forma de obfuscar el código es insertando ramas condicionales (declaraciones `if`, `else`, `switch`, `while`, etc),
de las cuales una nunca será ejecutada, pero no es fácil determinar cuál a primera vista.
Las ramas _"muertas"_ se llenan de código similar al código real para hacer difícil el proceso de deobfuscación.

Esta técnica muchas veces va acompañada del uso de _código muerto_. No se utiliza ramas condicionales en este caso,
sino que se inserta instrucciones, las cuales son ejecutadas, pero no tienen ninguna influencia sobre el resultado
o el funcionamiento del programa en general. La idea es confundir aún más a las personas tratando de reversar
el código.

Todo esto produce un código que parece ser muy complejo, con muchos caminos de ejecución, los cuales son
intencionalmente poco claros.

## ¿Cómo Deobfuscar Código?

Lamentablemente no existen una fórmula mágica para deobfuscar código obfuscado. Hay herramientas que pueden
ayudar a hacerlo, pero casi nunca logran obtener algo exactamente igual al código original.
Por esto, frecuentemente se debe hacer un análisis manual del código, revisando línea por línea y utilizando
múltiples deobfuscadores.

Los deobfuscadores normalmente están hechos para funcionar con un lenguaje en particular, y solo pueden
deobfuscar ciertas técnicas. A continuación se encuentra una lista de algunos deobfuscadores que les pueden ser
útiles, sin embargo, existen muchos otros que funcionan igual de bien o incluso mejor.

### JavaScript

* [de4js](https://lelinhtinh.github.io/de4js/)
* [JS Nice](http://jsnice.org/)
* [dCode](https://www.dcode.fr/javascript-unobfuscator)
* [Code Amaze](https://codeamaze.com/code-beautifier/javascript-deobfuscator)
* [Deobfuscate JavaScript](http://deobfuscatejavascript.com/)

### Python

* [Bytecode Simplifier](https://github.com/extremecoders-re/bytecode_simplifier)
* [deopy](https://pypi.org/project/deopy/) (Python3.6+)

### PHP

* [UnPHP](https://www.unphp.net/)
* [PHPDeobfuscator](https://github.com/simon816/PHPDeobfuscator)
* [FOPO PHP Deobfuscator](https://github.com/Antelox/FOPO-PHP-Deobfuscator)
* [PHP Deobfuscator](http://jonhburn2.freehostia.com/decode/)

### Java

* [Deobfuscator](https://github.com/java-deobfuscator/deobfuscator)
* [jdec](https://jdec.app/)
* [All-in-one deobfuscator](https://github.com/D3Hunter/deobfuscator)

### .NET

* [de4dot](https://github.com/de4dot/de4dot)
* [Lista de deobfuscadores opensource](https://github.com/NotPrab/.NET-Deobfuscator)
