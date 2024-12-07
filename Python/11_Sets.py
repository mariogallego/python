# Sets en Python
# Los sets (conjuntos) en Python son estructuras de datos que almacenan elementos únicos y no ordenados.
# Son muy útiles para trabajar con colecciones en las que no se desean duplicados
# y para realizar operaciones matemáticas como uniones, intersecciones y diferencias.

# Características principales de los sets:
# Elementos únicos: No se permiten duplicados. Si intentas añadir un elemento repetido, el set lo ignorará.
# No ordenados: No tienen un orden específico, por lo que no puedes acceder a los elementos mediante índices.
# Tipos inmutables: Solo puedes añadir elementos que sean inmutables (como números, strings o tuplas).

# Crear un set
mi_set = {1, 2, 3, 4, 5}
print(mi_set)  # Salida: {1, 2, 3, 4, 5}

# Crear un set vacío
set_vacio = set()
print(set_vacio)  # Salida: set()

# Eliminar duplicados automáticamente
set_con_duplicados = {1, 2, 2, 3, 4, 4, 5}
print(set_con_duplicados)  # Salida: {1, 2, 3, 4, 5}

# Crear un set a partir de una lista
set_desde_lista = set([1, 2, 3, 4, 4])
print(set_desde_lista)  # Salida: {1, 2, 3, 4}



# Operaciones básicas con sets
# 1. Añadir y eliminar elementos
mi_set = {1, 2, 3}

# Añadir un elemento
mi_set.add(4)
print(mi_set)  # Salida: {1, 2, 3, 4}

# Intentar añadir un elemento existente (no afecta al set)
mi_set.add(2)
print(mi_set)  # Salida: {1, 2, 3, 4}

# Eliminar un elemento existente
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4}

# Eliminar un elemento con seguridad (sin error si no existe)
mi_set.discard(10)  # No genera error
print(mi_set)  # Salida: {1, 2, 4}

# Eliminar y devolver un elemento aleatorio
elemento = mi_set.pop()
print(f"Elemento eliminado: {elemento}")
print(mi_set)  # Salida: {2, 4} (varía según el orden interno)

# Vaciar el set
mi_set.clear()
print(mi_set)  # Salida: set()



# 2. Operaciones de conjuntos (matemáticas)
# Unión (union o |)
# Une los elementos de dos sets, eliminando duplicados.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1.union(set2)  # Usando metodo
print(union)  # Salida: {1, 2, 3, 4, 5}

union_alt = set1 | set2  # Usando operador |
print(union_alt)  # Salida: {1, 2, 3, 4, 5}



# Intersección (intersection o &)
# Obtiene los elementos comunes entre dos sets.
interseccion = set1.intersection(set2)  # Usando metodo
print(interseccion)  # Salida: {3}

interseccion_alt = set1 & set2  # Usando operador &
print(interseccion_alt)  # Salida: {3}



# Diferencia (difference o -)
# Obtiene los elementos que están en el primer set, pero no en el segundo.
diferencia = set1.difference(set2)  # Usando metodo
print(diferencia)  # Salida: {1, 2}

diferencia_alt = set1 - set2  # Usando operador -
print(diferencia_alt)  # Salida: {1, 2}



# Diferencia simétrica (symmetric_difference o ^)
# Obtiene los elementos que están en un set o en el otro, pero no en ambos.
diferencia_simetrica = set1.symmetric_difference(set2)  # Usando metodo
print(diferencia_simetrica)  # Salida: {1, 2, 4, 5}

diferencia_simetrica_alt = set1 ^ set2  # Usando operador ^
print(diferencia_simetrica_alt)  # Salida: {1, 2, 4, 5}


# 3. Verificación de subconjuntos y superconjuntos
set1 = {1, 2, 3}
set2 = {1, 2}
set3 = {4, 5}

# Verificar si un set es subconjunto de otro
print(set2.issubset(set1))  # Salida: True
print(set3.issubset(set1))  # Salida: False

# Verificar si un set es superconjunto de otro
print(set1.issuperset(set2))  # Salida: True
print(set1.issuperset(set3))  # Salida: False


# 4. Comprobar pertenencia
mi_set = {1, 2, 3, 4}
print(3 in mi_set)  # Salida: True
print(5 in mi_set)  # Salida: False


#Métodos comunes de los sets
# Métodos comunes de los sets
# Metodo	Descripción
# add(elemento)	Añade un elemento al set.
# remove(elemento)	Elimina un elemento (genera error si no existe).
# discard(elemento)	Elimina un elemento (sin error si no existe).
# pop()	Elimina y devuelve un elemento aleatorio del set.
# clear()	Vacía el set.
# union(otro_set)	Devuelve la unión de dos sets.
# intersection(otro_set)	Devuelve la intersección de dos sets.
# difference(otro_set)	Devuelve la diferencia de dos sets.
# symmetric_difference(otro_set)	Devuelve la diferencia simétrica entre dos sets.
# issubset(otro_set)	Verifica si un set es subconjunto de otro.
# issuperset(otro_set)	Verifica si un set es superconjunto de otro.


# Ejemplo práctico: Eliminar duplicados de una lista
# Lista con duplicados
mi_lista = [1, 2, 2, 3, 4, 4, 5]

# Convertir la lista en un set para eliminar duplicados
mi_set = set(mi_lista)
print(mi_set)  # Salida: {1, 2, 3, 4, 5}

# Convertir de vuelta a lista
lista_sin_duplicados = list(mi_set)
print(lista_sin_duplicados)  # Salida: [1, 2, 3, 4, 5]
