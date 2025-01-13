palabra = 'python'
lista = [letra for letra in palabra]
print(lista)
for letra in palabra:
    print(letra)


pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)


# La comprensión de listas (o list comprehension) en Python es una forma concisa y poderosa de crear
# listas nuevas aplicando una expresión a cada elemento de un iterable, con la posibilidad de incluir condiciones.

# Sintaxis básica de comprensión de listas:
# nueva_lista = [expresión for elemento in iterable if condición]

# expresión: Lo que se añadirá a la nueva lista (puede ser una transformación del elemento original).
# elemento: Cada valor del iterable sobre el que se itera.
# iterable: Cualquier objeto iterable como listas, cadenas, rangos, etc.
# condición (opcional): Un filtro para incluir solo ciertos elementos.

# 1. Crear una lista con números del 1 al 10:
nueva_lista = [x for x in range(1, 11)]
print(nueva_lista)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Elevar al cuadrado los números del 1 al 10:
cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 3. Filtrar solo los números pares:
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8, 10]


# 4. Convertir una lista de cadenas a mayúsculas:
palabras = ["python", "es", "genial"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # Salida: ['PYTHON', 'ES', 'GENIAL']


# Con expresiones condicionales:
# Puedes usar un operador ternario dentro de la comprensión para incluir condiciones más avanzadas.
#
# 1. Reemplazar números impares con 0:
modificada = [x if x % 2 == 0 else 0 for x in range(1, 11)]
print(modificada)  # Salida: [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]


# Comprensiones anidadas:
# Puedes usar bucles anidados dentro de la comprensión de listas.
#
# 1. Crear una tabla de multiplicar:
tabla = [x * y for x in range(1, 4) for y in range(1, 4)]
print(tabla)  # Salida: [1, 2, 3, 2, 4, 6, 3, 6, 9]

# 2. Generar una matriz 2D (listas dentro de listas):
matriz = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print(matriz)  # Salida: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# Ventajas de las comprensiones de listas:
# Concisas: Puedes escribir en una línea lo que de otra manera requeriría múltiples líneas de código.
# Eficientes: Son más rápidas que los bucles for normales en muchos casos.
# Legibles: Expresan claramente la intención del programador.


# Ejemplo avanzado: Crear un diccionario con comprensión de listas:
# Aunque es más común usar dict comprehensions, puedes transformar una lista en un diccionario.
lista = ["a", "b", "c"]
diccionario = {x: x.upper() for x in lista}
print(diccionario)  # Salida: {'a': 'A', 'b': 'B', 'c': 'C'}















