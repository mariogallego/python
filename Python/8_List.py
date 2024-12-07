
# Creación de listas
# Lista vacía
lista_vacia = []

# Lista de números
lista_numeros = [1, 2, 3, 4]

# Lista de cadenas
lista_cadenas = ["Python", "es", "genial"]

# Lista con tipos mixtos
lista_mixta = [1, "Python", True, 3.14]

# Lista dentro de otra lista (anidada)
lista_anidada = [[1, 2], ["a", "b"]]



# Operaciones básicas con listas
# Acceso por índice
lista = ["a", "b", "c", "d"]
print(lista[0])   # 'a' (primer elemento)
print(lista[-1])  # 'd' (último elemento)


# Slicing
lista = [0, 1, 2, 3, 4, 5]
print(lista[1:4])  # [1, 2, 3] (desde índice 1 hasta 3)
print(lista[:3])   # [0, 1, 2] (desde el inicio hasta índice 2)
print(lista[3:])   # [3, 4, 5] (desde índice 3 hasta el final)
print(lista[::-1]) # [5, 4, 3, 2, 1, 0] (lista invertida)


# Modificar elementos
lista = [10, 20, 30]
lista[1] = 99
print(lista)  # [10, 99, 30]


# Longitud de una lista
lista = [1, 2, 3, 4]
print(len(lista))  # 4



# Concatenación y repetición
lista1 = [1, 2]
lista2 = [3, 4]
print(lista1 + lista2)  # [1, 2, 3, 4]
print(lista1 * 3)       # [1, 2, 1, 2, 1, 2]


# Pertenencia
lista = [1, 2, 3, 4]
print(2 in lista)     # True
print(5 not in lista) # True


# Iterar sobre listas
lista = [1, 2, 3, 4]

# Con un bucle for
for elemento in lista:
    print(elemento)

# Con índices
for i in range(len(lista)):
    print(lista[i])


# Listas anidadas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos
print(matriz[0][1])  # 2 (fila 0, columna 1)

# Recorrer una matriz
for fila in matriz:
    for elemento in fila:
        print(elemento)



# Comprensiones de listas
# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]

# Filtrar elementos
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]































