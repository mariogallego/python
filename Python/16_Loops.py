# 1. Bucle for
# El bucle for itera sobre los elementos de una secuencia (como una lista, tupla, cadena o rango)
# y ejecuta un bloque de código por cada elemento.
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
# Salida:
# 1
# 2
# 3
# 4
# 5


palabra = "Python"
for letra in palabra:
    print(letra)
# Salida:
# P
# y
# t
# h
# o
# n

for i in range(5):  # Genera números del 0 al 4
    print(i)
# Salida:
# 0
# 1
# 2
# 3
# 4





# 2. Bucle while
# El bucle while ejecuta un bloque de código mientras una condición sea verdadera.
# Es útil cuando no se sabe de antemano cuántas veces se repetirá el bucle.
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa el contador para evitar bucles infinitos
# Salida:
# 0
# 1
# 2
# 3
# 4



# 3. Control avanzado dentro de bucles
# 3.1. break
# Termina un bucle antes de que complete todas sus iteraciones.
for numero in range(10):
    if numero == 5:
        break  # Sale del bucle cuando el número es 5
    print(numero)
# Salida:
# 0
# 1
# 2
# 3
# 4



# 3.2. continue
# Salta a la siguiente iteración del bucle sin ejecutar el resto del código en la iteración actual.
#
# Ejemplo
for numero in range(10):
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)
# Salida:
# 1
# 3
# 5
# 7
# 9


# 3.3. else en bucles
# Un bloque else se ejecuta después de un bucle si este no se interrumpe con un break.
for numero in range(5):
    if numero == 3:
        break
    print(numero)
else:
    print("El bucle terminó sin interrupciones")  # Esto no se ejecuta

# Salida:
# 0
# 1
# 2

# Ejemplo con while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle terminó normalmente")
# Salida:
# 0
# 1
# 2
# 3
# 4
# El bucle terminó normalmente






























