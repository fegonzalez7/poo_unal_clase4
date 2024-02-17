# Programación Orientada a Objetos - UNAL

## Clase 3: Resumen de Conceptos Clave en Python pt. 2

## Bucles - Ciclos

### Ciclo `while`

El ciclo `while` ejecuta un bloque de instrucciones mientras una condición booleana sea verdadera.

```python
i: int = 0
while(i <= 6): 
  print(i)
  i = i + 1 # Similar a i += 1
```
*Resultado por terminal:*
```
0
1
2
3
4
5
6
```

### Componentes del Ciclo `while`
- Condición de parada: Evalúa si el bloque de instrucciones debe ejecutarse.
- Bloque de instrucciones: Conjunto de instrucciones que se ejecutan mientras la condición sea verdadera.
- Actualización: Modificación de variables para que eventualmente la condición de parada sea falsa y termine el ciclo.

### Ciclo `do-while`
Python no tiene un ciclo `do-while` nativo, pero se puede simular usando una bandera junto con while.

```python
flag: bool = True
while flag or <condicion>:
  flag = False
  # Bloque de instrucciones
```

```python
flag: bool = True
while flag or (num < 65 or num > 90):
  flag = False
  num = int(input("Ingrese un entero: "))
  print("El entero corresponde al caracter " + chr(num))
```

*Resultado por terminal:* (Cuando el usuario ingresa 70 como input)
```
Ingrese un entero: 70
El entero corresponde al caracter F
```


### break y continue
- `continue`: Salta a la siguiente iteración del ciclo.
- `break`: Termina el ciclo inmediatamente.

```python
i: int = 0
while(i < 10): 
  i += 1 
  if i == 5: 
    continue
  print(i)
```
*Resultado por consola:*
```
1
2
3
4
6
7
8
9
10
```

```python
sumatory: int = 0 # Ojo con usar palabras reservadas del lenguaje
while True:
  num = int(input("Ingrese un entero o 0 para salir: "))
  if num == 0:
    break
  sumatory += num
print("La suma de los numeros ingresados es " + str(sumatory))
```
*resultado por consola:* (Cuando el usuario ingresa 8, 5, 6, 6, 0)
```
Ingrese un entero o 0 para salir: 8
Ingrese un entero o 0 para salir: 5
Ingrese un entero o 0 para salir: 6
Ingrese un entero o 0 para salir: 6
Ingrese un entero o 0 para salir: 0
La suma de los numeros ingresados es 25
```

### Ciclo `for`

El ciclo `for` en Python itera sobre los elementos de cualquier secuencia (una lista o una cadena de texto), en el orden que aparecen en la secuencia.

```python
for <elemento> in <coleccion>:
    # Bloque de código a ejecutar
```
#### **Ejemplo 1:**
```python
fruits = ["Tomate de arbol", "Maracuya", "Guayaba"]
for f in fruits:
    print(f)
```

*Resultado por consola:*
````
Tomate de arbol
Maracuya
Guaya
````
#### **Ejemplo 2:**
```python
# Operador in - pertenencia
fruits = ["Tomate de arbol", "Maracuya", "Guayaba"]
print("Maracuya" in fruits)  # Salida: True
print("Fresa" in fruits)     # Salida: False
```
#### **Ejemplo 3:**
```python
fruits = ["Pera", "Maracuya", "Guayaba", "Lulo", "Granadilla"]
for f in fruits:
    print(f)
    if f == "Guayaba":
        break  # Termina el ciclo
```

*Resultado por consola:*
```
Pera
Maracuya
Guayaba
```

### Ranges
La función range() devuelve una secuencia de números, comenzando desde 0 por defecto, e incrementa en 1 (por defecto), y termina en un número especificado.
#### **Ejemplo 1:**
```python
for num in range(6):
    print(num)
```

*Resultado por consola:*
```
0
1
2
3
4
5
```
#### **Ejemplo 2:**
```python
for num in range(-2, 8, 2):
    print(num)
```

*Resultado por consola:*
```
-2
0
2
4
6
```

## Listas

Las listas en Python son secuencias de elementos que pueden almacenar datos heterogéneos, incluyendo otros arreglos o listas. La mutabilidad es una característica clave de las listas, permitiendo modificarlas tras su definición.

```python
empty_list = []
mixed_list = [1, "dos", 3.0, [4, "cinco"]]
```

### Acceso y Modificación
 - **Acceso:** Se realiza mediante el índice del elemento, comenzando por 0.
 - **Modificación:** Puedes cambiar el valor de un elemento directamente utilizando su índice.

 ```python
# Acceso
first_element = mixed_list[0] # Salida: 1

# Modificación
mixed_list[1] = "dos modificado" # Nuevo valor de la lista [[1, "dos modificado", 3.0, [4, "cinco"]]]
```

### Operaciones Principales en Listas
#### Concatenación
Operador `+`: Une dos listas.

 ```python
new_list = [1, 2, 3] + [4, 5, 6]
 ```

 *Resultado:*
 ```
 [1, 2, 3, 4, 5, 6]
 ```

#### Repetición
Operador `*`: Repite los elementos de una lista un número determinado de veces.

 ```python
repeated_list = [1, 2, 3] * 2
```

*Resultado:*
```
[1, 2, 3, 1, 2, 3]
```

#### Indexación y Slicing
 - Indexación: Acceder a un elemento específico.
 - Slicing: Obtener una sublista utilizando [inicio:fin:incremento].

 ```python
# Indexación
element = mixed_list[1]
# Slicing
sublist = mixed_list[1:3]
```

*Resultado:*
```python
## en la asignación variables
element = 'dos'
sublist = ['dos', 3.0]
```

**Métodos Útiles**
- `append(<elemento>)`: Agrega un elemento al final.
- `pop([<índice>])`: Elimina y retorna un elemento por índice.
- `insert(<índice>, <elemento>)`: Inserta un elemento en una posición.
- `remove(<elemento>)`: Elimina la primera aparición de un elemento.
- `sort([reverse=<bool>])`: Ordena los elementos de la lista.

### Recorrido de Listas
Uso del Ciclo `for`.
#### Ejemplo 1:
 ```python
for element in mixed_list:
    print(element)
```

*Resultado por consola:*
```
1
dos
3.0
[4, 'cinco']
```
#### Ejemplo 2:
 ```python
i: int  = 0
while i < len(mixed_list):
    print(mixed_list[i])
    i += 1
```

*resultado por consola:*
```
1
dos
3.0
[4, 'cinco']
```

### List comprehensions
Permiten crear listas de manera concisa a partir de una secuencia existente.

 ```python
cubes = [x**3 for x in range(5)]
```

*Resultado:*
```python
## En la asignación de la variable

cubes = [0, 1, 8, 27, 64]
```

## Funciones (otra vez)
### Funciones Recursivas
Una función recursiva se llama a sí misma para resolver un problema. Debe tener un caso base para terminar la recursión y un caso recursivo que se acerque al caso base.

```python
def recursive_factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
```

### Funciones Lambda (Anónimas)
Las funciones lambda permiten definir funciones pequeñas y anónimas en una sola línea.

```python
if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  sumatory = (lambda x, y: x + y)(a,b)
  print("La suma de " + str(a) + " y " + str(b) + " es " + str(sumatory))
  #print(f"La suma de {a} y {b} es {sumatory}") -> Otro método
```

*Resultado por consola:* (Cuando el usuario ingresa los valores 6, 5)
```
Ingrese numero a: 6
Ingrese numero b: 5
La suma de 6 y 5 es 11
```

### Argumentos por Defecto
Permiten definir funciones con argumentos que tienen un valor predeterminado.

```python
def greet(name, message="Hola"):
    print(f"{message}, {name}!")

greet("Mundo")  # Usa el mensaje por defecto
greet("Mundo", "Adiós")  # Usa el mensaje proporcionado
```

*Resultado por consola:*
```
Hola, Mundo!
Adiós, Mundo!
```

### Argumentos No Definidos (*args)
Permiten definir funciones que aceptan un número variable de argumentos.

```python
def addAll(*args):
    return sum(args)

print(addAll(1, 2, 3, 4))
```
*Resultado por consola:* `10`


-----

## Reto 1
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_1 en slack.

1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. *entrada:* `(1,2,"+")`, *salida* `(3)`.

2. Realice una función que permita validar si una palabra es un palíndromo. **Condición:** No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`

**P.D.** El repositorio debe tener los archivos .py de los 5 puntos, uno por cada ejercicio. Asimismo una corta explicación de como llego a la solución.



