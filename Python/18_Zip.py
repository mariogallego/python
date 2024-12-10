# La función zip() en Python combina elementos de dos o más iterables (como listas, tuplas o cadenas) en pares,
# creando un nuevo iterable donde cada elemento es una tupla que contiene los valores
# correspondientes de los iterables originales.

nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]

# Combina los nombres con las edades
combinado = zip(nombres, edades)

# Convierte a lista para verlo claramente
print(list(combinado))


# Ejemplo con Diferentes Longitudes
# Si los iterables tienen longitudes diferentes, zip() trunca el resultado al tamaño del iterable más corto.
nombres = ["Ana", "Luis"]
edades = [25, 30, 35]  # Tiene un elemento más

combinado = zip(nombres, edades)

print(list(combinado))


# Desempaquetar un Objeto zip
# Puedes iterar directamente sobre el objeto zip en un bucle.
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")


# Combinar Más de Dos Iterables
# Puedes usar zip() con más de dos iterables.
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]
ciudades = ["Madrid", "Barcelona", "Valencia"]

combinado = zip(nombres, edades, ciudades)

print(list(combinado))

# Ejemplo de Uso con Diccionarios
# Puedes usar zip para crear un diccionario combinando dos listas: una con claves y otra con valores.
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 25, "Madrid"]

diccionario = dict(zip(claves, valores))
print(diccionario)



# Invertir un Objeto zip
# Puedes "desempaquetar" un objeto zip usando el operador * para invertirlo.

nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]

# Crear un objeto zip
combinado = zip(nombres, edades)

# Desempaquetar con *
nombres_desempaquetados, edades_desempaquetadas = zip(*combinado)

print(nombres_desempaquetados)  # ('Ana', 'Luis', 'Carlos')
print(edades_desempaquetadas)  # (25, 30, 35)



# Ejemplo Práctico: Comparar Dos Listas
# Puedes usar zip para comparar elementos de dos listas.
lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 0, 4]

for a, b in zip(lista1, lista2):
    if a == b:
        print(f"{a} y {b} son iguales")
    else:
        print(f"{a} y {b} son diferentes")



# Usar zip() con List Comprehensions
# Puedes combinar zip con comprensiones para generar listas o diccionarios.
#
# Ejemplo: Filtrar Pares
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]

# Crear lista de combinaciones donde la edad es mayor a 28
resultado = [(nombre, edad) for nombre, edad in zip(nombres, edades) if edad > 28]
print(resultado)

