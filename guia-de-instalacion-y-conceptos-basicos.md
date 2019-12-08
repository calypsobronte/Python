## ¿Qué es Python?
Python es un lenguaje de programación creado por [Guido Van Rossum],con una sintaxis muy limpia, ideado para enseñar a programar bien. Se trata de un lenguaje interpretado de tipado dinámico cuya sintaxis se basa en tener un código legible. Se trata de un lenguaje de programación multiparadigma y disponible en varias plataformas.⁣

## Instalación

Se recomienda instalar la version **2.7** por ser la mas estable.
> ActualmentePython tiene dos versiones con un gran uso: **Python 2.x** y **Python 3.x**

### Windows
Ingresamos a [python.org/windows] el sitio reconocera el sistema operativo.
> Nota: cuando descargues el ejecutable, sigue los pasos de instalación.

### MacOS
**Python** viene con **OS X**, por lo que probablemente no necesites hacer este paso. Puede verificar esto escribiendo `python --version` en la Terminal.

Si por alguna razón no tiene Python o si desea obtener la versión actual, ¡ahora puede hacerlo fácilmente con [Homebrew]!.
```bash
$ brew install python
```
### Linux
Python en linux en la mayoria de los casos viene instalado por default puedes verificar utilizando el siguiente comando
```bash
$ python -V
```
Si te arroja error, quiere decir que python no esta instalado en nuestra maquina, por lo tanto puedes insgresar estos comandos:

#### Ubuntu o Debian
```bash
$ sudo apt-get install python3.1
```
#### Red Hat o Centos
```bash
$ sudo yum install python
```
#### Arch Linux o Manjaro
```bash
$ sudo pacman -S python
```

## Tipos de datos en Python

- **Enteros (int):** en este grupo están todos los números, enteros y long:
ejemplo: `1`, `2`, `3`, `2121`, `2192`, `-123`

- **Booleanos (bool):** Son los valores falso o verdadero, compatibles con todas las operaciones booleanas ( `and`, `not`, `or` ):
ejemplo: True, False

- **Cadenas (str):** Son una cadena de texto : “Hola”, “¿Cómo estas?”

- **Listas:** Son un grupo o array de datos, puede contener cualquiera de los datos anteriores:
ejemplos: `[1,2,3, ”hola” , [1,2,3] ]`, `[1,“Hola”,True ]`
    ```python
    >>> L = [22, True, ”una lista”, [1, 2]]
    >>> L[0]
    22
    ```

- **Diccionarios:** Son un grupo de datos que se acceden a partir de una clave:
ejemplo: {"clave":"valor"}, {"nombre":"Lina"}
    ```python
    >>> D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"}
    >>> D["Amelie"]
    "Jean-Pierre Jeunet"
    ```

- **Tuplas:** también son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar.
ejemplos: `(1,2,3, ”hola” , (1,2,3) )`, `(1,“Hola”,True)` (Pero jamás podremos cambiar los elementos dentro de esa Tupla)
    ```python
    >>> T = (22, True, "una tupla", (1, 2))
    >>> T[0]
    22
    ```
    > En Python trabajas con módulos y ficheros que usas para importar las librerías.

## Funciones

Las funciones las defines con def junto a un nombre y unos paréntesis que reciben los parámetros a usar. Terminas con dos puntos.

`def nombre_de_la_función(parametros):`

Después por indentación colocas los datos que se ejecutarán desde la función
```python
 $ python
 >>> def first_function_calypsobronte():
 ...	return “Hello World!”
 ...
 >>> first_function_calypsobronte()
 'Hello World!'
 >>>
 ```


[Guido Van Rossum]: https://en.wikipedia.org/wiki/Guido_van_Rossum
[python.org/windows]: https://www.python.org/downloads/release/python-2716/
[Homebrew]: https://brew.sh/