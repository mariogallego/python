# Ejemplo combinado
# Puedes combinar varios operadores en condiciones lógicas con and, or, y not:
x = 10
y = 20
z = 10

print(x == z and x < y)  # True (x es igual a z y menor que y)
print(x != y or x > z)   # True (x es diferente de y o mayor que z)
print(not (x > y))       # True (x no es mayor que y)

mi_bool = 10!=5
print(mi_bool)


# 1. Comparar listas, cadenas o tuplas
# Los operadores de comparación funcionan también con estructuras como listas, cadenas y tuplas.
# Comparar cadenas
print("Python" == "Python")   # True
print("Python" < "pythons")   # True (comparación lexicográfica)

# Comparar listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(lista1 == lista2)       # True (contenido idéntico)

# Comparar tuplas
tupla1 = (1, 2)
tupla2 = (1, 3)
print(tupla1 < tupla2)        # True (1 == 1, pero 2 < 3)


# 2. Comparar objetos personalizados
# Puedes personalizar las comparaciones definiendo métodos especiales como __eq__, __lt__, etc., en clases.


# 3. Comparaciones en listas con comprensión
# Puedes usar comparaciones dentro de listas por comprensión para filtrar valores.
numeros = [10, 20, 30, 40, 50]
filtrados = [n for n in numeros if n > 25]
print(filtrados)  # [30, 40, 50]


# 4. Comparar usando el operador ternario
# Los operadores de comparación son útiles en expresiones condicionales de una sola línea.
a, b = 15, 20
resultado = "Mayor" if a > b else "Menor o Igual"

print(resultado)  # "Menor o Igual"


# 5. Comparar números con tolerancia (flotantes)
# En cálculos matemáticos con flotantes, comparar directamente puede ser problemático debido a imprecisiones. Usa una tolerancia.

# 6. Usar all() y any() en comparaciones
# Las funciones all() y any() permiten verificar múltiples condiciones de forma compacta.
valores = [3, 6, 9]

# Comprobar si todos son mayores que 2
print(all(v > 2 for v in valores))  # True

# Comprobar si al menos uno es mayor que 8
print(any(v > 8 for v in valores))  # True



#7. Comparaciones en algoritmos complejos (búsqueda del mínimo/máximo)
# Combina comparaciones con estructuras como diccionarios.




# 8. Comparar fechas u objetos avanzados
# Si trabajas con fechas (por ejemplo, con datetime), puedes usar comparaciones directamente.
from datetime import datetime

hoy = datetime.now()
evento = datetime(2024, 12, 25)

if evento > hoy:
    print("El evento es en el futuro.")
else:
    print("El evento ya pasó.")







