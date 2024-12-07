# Index
# 1. Uso del metodo index() con listas
# lista.index(valor, inicio, fin)
# valor: El elemento que deseas buscar.
# inicio (opcional): El índice desde donde iniciar la búsqueda.
# fin (opcional): El índice hasta donde buscar.

# Lista simple
mi_lista = [10, 20, 30, 40, 50]

print(mi_lista.index(30))  # Resultado: 2 (índice del elemento 30)

mi_lista = [10, 20, 30, 20, 50]

# Buscar el 20 desde el índice 2 en adelante
print(mi_lista.index(20, 2))  # Resultado: 3

# Buscar entre un rango de índices
print(mi_lista.index(50, 2, 5))  # Resultado: 4

mi_lista = [10, 20, 30]
# print(mi_lista.index(40))  # Lanza: ValueError: 40 is not in list



# 2. Uso del metodo index() con cadenas
# cadena.index(subcadena, inicio, fin)
# subcadena: La subcadena que deseas buscar.
# inicio (opcional): El índice desde donde iniciar la búsqueda.
# fin (opcional): El índice hasta donde buscar.
# Cadena simple
mi_cadena = "Hola mundo"

print(mi_cadena.index("mundo"))  # Resultado: 5 (la 'm' comienza en el índice 5)

# Buscar con parámetros opcionales
print(mi_cadena.index("o", 6))   # Resultado: 9 (busca 'o' desde el índice 6)

print("Positivo: " + mi_cadena[2])
print("Negativo: " + mi_cadena[-2]) #con valor negativo cuenta desde la derecha

# tuplas
mi_tupla = (1, 2, 3, 4, 5)

print(mi_tupla.index(3))  # Resultado: 2


# index vs find
# find devuelve -1 en caso de que no exista
mi_cadena = "Hola mundo"
print(mi_cadena.find("python"))  # Resultado: -1 (en vez de lanzar error)



# Conclusión
# El metodo index() es útil para localizar la posición de un elemento,
# pero ten cuidado al usarlo con elementos que podrían no estar presentes.
# Si quieres evitar errores, asegúrate de verificar antes si el elemento existe, por ejemplo, usando in:

lista = [10, 20, 30]
if 40 in lista:
    print(lista.index(40))
else:
    print("El elemento no está en la lista.")












