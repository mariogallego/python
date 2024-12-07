from math import isqrt

mi_bool_1 = True
mi_bool_2 = False

lista = [1,2,3]
print(4 in lista)
print(4 not in lista)

print(isqrt(25)==5)


# Operadores que devuelven valores booleanos
# 1. Operadores de comparación
# Los operadores de comparación siempre devuelven un valor booleano (True o False).
#
# Operador	Descripción	Ejemplo
# ==	Igual a	5 == 5 → True
# !=	No igual a	5 != 3 → True
# >	Mayor que	5 > 3 → True
# <	Menor que	3 < 5 → True
# >=	Mayor o igual que	5 >= 5 → True
# <=	Menor o igual que	3 <= 5 → True



# 2. Operadores lógicos
# Los operadores lógicos permiten combinar valores booleanos.
#
# Operador	Descripción	Ejemplo
# and	Devuelve True si ambos operandos son True	(5 > 3) and (3 > 1) → True
# or	Devuelve True si al menos un operando es True	(5 > 3) or (3 < 1) → True
# not	Invierte el valor booleano	not (5 > 3) → False
a = True
b = False

print(a and b)  # Salida: False
print(a or b)   # Salida: True
print(not a)    # Salida: False



# 3. Operadores de pertenencia
# Se utilizan para verificar si un elemento está o no en una colección.
#
# Operador	Descripción	Ejemplo
# in	Devuelve True si el elemento está en la colección	'a' in 'hola' → True
# not in	Devuelve True si el elemento no está en la colección	'z' not in 'hola' → True


cadena = "hola"
print('h' in cadena)    # Salida: True
print('z' not in cadena)  # Salida: True


# 4. Operadores de identidad
# Verifican si dos variables hacen referencia al mismo objeto.
#
# Operador	Descripción	Ejemplo
# is	Devuelve True si las variables son el mismo objeto	a is b
# is not	Devuelve True si las variables no son el mismo objeto	a is not b
a = [1, 2, 3]
b = a  # Ambas variables apuntan al mismo objeto
c = [1, 2, 3]  # Nuevo objeto con el mismo contenido

print(a is b)  # Salida: True
print(a is c)  # Salida: False
print(a == c)  # Salida: True (el contenido es igual)

# Conversión a Booleanos (bool())
# Cualquier valor en Python puede evaluarse como un valor booleano usando la función bool(). Las reglas generales son:
#
# False en contexto booleano:
#
# 0 (número entero o flotante)
# None
# Cadenas vacías: ""
# Colecciones vacías: [], {}, set(), tuple()
# True en contexto booleano:
#
# Cualquier valor que no sea considerado "vacío" (como números diferentes de 0, cadenas no vacías, etc.)
print(bool(0))          # Salida: False
print(bool(1))          # Salida: True
print(bool(-5))         # Salida: True
print(bool(""))         # Salida: False
print(bool("Python"))   # Salida: True
print(bool([]))         # Salida: False
print(bool([1, 2, 3]))  # Salida: True



# Uso en estructuras de control
# Los booleanos son fundamentales en estructuras como condicionales y bucles.
#
# Ejemplo:
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# Salida: Eres mayor de edad

# Uso en bucles
while True:
    print("Este bucle se detendrá.")
    break  # Detener el bucle




# Resumen de valores que evalúan a False
# None
# False
# 0, 0.0, 0j (cero entero, flotante o complejo)
# Cadenas vacías: ""
# Colecciones vacías: [], {}, set(), tuple()
# Cualquier otro valor evalúa a True.











