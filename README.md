# Programación Orientada a Objetos - UNAL

## Clase 3: Resumen de Conceptos Clave en Python pt. 2

## Bucles - Ciclos

### Ciclo `while`

El ciclo `while` ejecuta un bloque de instrucciones mientras una condición booleana sea verdadera.

```python
i = 0
while(i <= 6):
  print(i)
  i = i + 1
```

### Componentes del Ciclo `while`
- Condición de parada: Evalúa si el bloque de instrucciones debe ejecutarse.
- Bloque de instrucciones: Conjunto de instrucciones que se ejecutan mientras la condición sea verdadera.
- Actualización: Modificación de variables para que eventualmente la condición de parada sea falsa y termine el ciclo.

### Ciclo `do-while`
Python no tiene un ciclo `do-while` nativo, pero se puede simular usando una bandera junto con while.

```python
bandera = True
while bandera or condicion:
  bandera = False
  # Bloque de instrucciones
```

```python
bandera = True
while bandera or (num < 65 or num > 90):
  bandera = False
  num = int(input("Ingrese un entero: "))
  print("El entero corresponde al caracter " + chr(num))
```

### break y continue
- `continue`: Salta a la siguiente iteración del ciclo.
- `break`: Termina el ciclo inmediatamente.

```python
i = 0
while(i < 10): 
  i += 1 
  if i == 5: 
    continue
  print(i)
```

```python
sum = 0
while True:
  num = int(input("Ingrese un entero o 0 para salir: "))
  if num == 0:
    break
  sum += num
print("La suma de los numeros ingresados es " + str(sum))
```

### Ciclo `for`

El ciclo `for` en Python itera sobre los elementos de cualquier secuencia (una lista o una cadena de texto), en el orden que aparecen en la secuencia.

```python
for elemento in coleccion:
    # Bloque de código a ejecutar
```

```python
frutas = ["Tomate de arbol", "Maracuya", "Guayaba"]
for f in frutas:
    print(f)
```

```python
# Operador in - pertenencia
frutas = ["Tomate de arbol", "Maracuya", "Guayaba"]
print("Maracuya" in frutas)  # Salida: True
print("Fresa" in frutas)     # Salida: False
```

```python
frutas = ["Pera", "Maracuya", "Guayaba", "Lulo", "Granadilla"]
for f in frutas:
    print(f)
    if f == "Guayaba":
        break  # Termina el ciclo
```

### Ranges
La función range() devuelve una secuencia de números, comenzando desde 0 por defecto, e incrementa en 1 (por defecto), y termina en un número especificado.

```python
for num in range(6):
    print(num)
```

```python
for num in range(-2, 8, 2):
    print(num)
```

## Listas

Las listas en Python son secuencias de elementos que pueden almacenar datos heterogéneos, incluyendo otros arreglos o listas. La mutabilidad es una característica clave de las listas, permitiendo modificarlas tras su definición.

```python
lista_vacia = []
lista_mixta = [1, "dos", 3.0, [4, "cinco"]]
```

### Acceso y Modificación
 - **Acceso:** Se realiza mediante el índice del elemento, comenzando por 0.
 - **Modificación:** Puedes cambiar el valor de un elemento directamente utilizando su índice.

 ```python
# Acceso
primer_elemento = lista_mixta[0]

# Modificación
lista_mixta[1] = "dos modificado"
```

### Operaciones Principales en Listas
#### Concatenación
Operador `+`: Une dos listas.

 ```python
lista_nueva = [1, 2, 3] + [4, 5, 6]

#### Repetición
Operador `*`: Repite los elementos de una lista un número determinado de veces.

 ```python
lista_repetida = [1, 2, 3] * 2
```

#### Indexación y Slicing
 - Indexación: Acceder a un elemento específico.
 - Slicing: Obtener una sublista utilizando [inicio:fin:incremento].

 ```python
# Indexación
elemento = lista_mixta[1]
# Slicing
sublista = lista_mixta[1:3]
```

**Métodos Útiles**
- `append(elemento)`: Agrega un elemento al final.
- `pop([índice])`: Elimina y retorna un elemento por índice.
- `insert(índice, elemento)`: Inserta un elemento en una posición.
- `remove(elemento)`: Elimina la primera aparición de un elemento.
- `sort([reverse=bool])`: Ordena los elementos de la lista.

### Recorrido de Listas
Uso del Ciclo `for`.

 ```python
for elemento in lista_mixta:
    print(elemento)
```

 ```python
i = 0
while i < len(lista_mixta):
    print(lista_mixta[i])
    i += 1
```

### List comprehensions
Permiten crear listas de manera concisa a partir de una secuencia existente.

 ```python
cubos = [x**3 for x in range(5)]
```

## Funciones (otra vez)
### Funciones Recursivas
Una función recursiva se llama a sí misma para resolver un problema. Debe tener un caso base para terminar la recursión y un caso recursivo que se acerque al caso base.

```python
def factorialRecursivo(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorialRecursivo(n-1)
```

### Funciones Lambda (Anónimas)
Las funciones lambda permiten definir funciones pequeñas y anónimas en una sola línea.

```python
if __name__ == "__main__":
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  suma = (lambda x, y: x + y)(a,b)
  print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma))
```

### Argumentos por Defecto
Permiten definir funciones con argumentos que tienen un valor predeterminado.

```python
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}!")

saludar("Mundo")  # Usa el mensaje por defecto
saludar("Mundo", "Adiós")  # Usa el mensaje proporcionado
```

### Argumentos No Definidos (*args)
Permiten definir funciones que aceptan un número variable de argumentos.

```python
def sumarTodos(*args):
    return sum(args)

print(sumarTodos(1, 2, 3, 4))
```

-----

## Reto 1
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_1 en slack.


