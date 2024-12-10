# El enumerador en Python se utiliza con la función incorporada enumerate().
# Esta función permite iterar sobre un iterable (como una lista, tupla o cadena) y,
# al mismo tiempo, proporciona un índice para cada elemento.

# Sintaxis de enumerate()
# enumerate(iterable, start=0)

# Parámetros:
# iterable: Cualquier objeto iterable como una lista, cadena, tupla, etc.
# start (opcional): El índice inicial (por defecto es 0).

frutas = ["manzana", "pera", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")



# Ejemplo con start personalizado
# Puedes cambiar el índice inicial usando el argumento start.
frutas = ["manzana", "pera", "naranja"]

for indice, fruta in enumerate(frutas, start=1):
    print(f"Índice: {indice}, Fruta: {fruta}")



# Aplicaciones comunes
# 1. Modificar elementos en una lista
# Puedes usar enumerate para iterar por índice y valor al mismo tiempo y modificar la lista.
frutas = ["manzana", "pera", "naranja"]

for indice, fruta in enumerate(frutas):
    frutas[indice] = fruta.upper()  # Convertir a mayúsculas

print(frutas)




# 2. Crear un diccionario a partir de una lista
# Puedes usar enumerate para crear un diccionario donde las claves sean los índices.
frutas = ["manzana", "pera", "naranja"]

frutas_dict = {indice: fruta for indice, fruta in enumerate(frutas)}

print(frutas_dict)



# 3. Buscar elementos con su índice
# Si necesitas identificar elementos en una lista con su posición, enumerate es ideal.

numeros = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros):
    if numero == 30:
        print(f"El número 30 está en el índice {indice}")




# Ejemplo Completo: Enumerar con condiciones

frutas = ["manzana", "pera", "naranja", "uva"]

for indice, fruta in enumerate(frutas):
    if "naranja" in fruta:
        print(f"La fruta '{fruta}' está en el índice {indice}")
















