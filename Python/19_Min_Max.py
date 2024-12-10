# Las funciones min() y max() en Python se utilizan para encontrar el valor mínimo o máximo de un iterable,
# o entre dos o más valores específicos. Son funciones incorporadas y ampliamente utilizadas por su simplicidad y versatilidad.

# 1. min()
# La función min() devuelve el menor elemento de un iterable o el menor de dos o más valores.
numeros = [5, 3, 9, 1, 4]
print(min(numeros))  # Salida: 1

print(min(5, 3, 9, 1, 4))  # Salida: 1



# 2. max()
# La función max() devuelve el mayor elemento de un iterable o el mayor de dos o más valores.
numeros = [5, 3, 9, 1, 4]
print(max(numeros))  # Salida: 9

print(max(5, 3, 9, 1, 4))  # Salida: 9


# 3. Uso de key en min() y max()
# El parámetro key permite especificar una función que determina cómo se evalúan los valores para encontrar el mínimo o máximo.
#
# Ejemplo con cadenas

palabras = ["manzana", "pera", "naranja", "uva"]
print(min(palabras, key=len))  # Palabra más corta: "uva"
print(max(palabras, key=len))  # Palabra más larga: "manzana"



# Ejemplo con diccionarios
# Si tienes un diccionario, puedes usar el parámetro key para encontrar el mínimo o máximo basado en las claves o valores.
edades = {"Ana": 25, "Luis": 30, "Carlos": 20}

# Persona más joven
print(min(edades, key=edades.get))  # Salida: "Carlos"

# Persona mayor
print(max(edades, key=edades.get))  # Salida: "Luis"



# Ejemplo con tuplas
# Puedes encontrar el mínimo o máximo de una lista de tuplas basada en un elemento específico.
puntos = [(1, 2), (3, 1), (5, 0), (2, 4)]

# Encontrar el punto con la coordenada x más baja
print(min(puntos, key=lambda punto: punto[0]))  # Salida: (1, 2)

# Encontrar el punto con la coordenada y más alta
print(max(puntos, key=lambda punto: punto[1]))  # Salida: (2, 4)





# 4. Valores Especiales
# Cadenas
# Para cadenas, min() y max() evalúan con base en el orden alfabético (ASCII).
texto = "python"
print(min(texto))  # Letra más pequeña: "h"
print(max(texto))  # Letra más grande: "y"


# Listas vacías
# Si pasas un iterable vacío a min() o max(), obtendrás un error ValueError.
# print(min([]))  # Error: ValueError
# print(max([]))  # Error: ValueError


print(min([], default=0))  # Salida: 0
print(max([], default=0))  # Salida: 0




# Comparar elementos personalizados
# Si tienes objetos personalizados, puedes usar el parámetro key para especificar cómo deben compararse.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

personas = [
    Persona("Ana", 25),
    Persona("Luis", 30),
    Persona("Carlos", 20),
]

# Persona más joven
joven = min(personas, key=lambda p: p.edad)
print(joven.nombre)  # Salida: "Carlos"

# Persona mayor
mayor = max(personas, key=lambda p: p.edad)
print(mayor.nombre)  # Salida: "Luis"


