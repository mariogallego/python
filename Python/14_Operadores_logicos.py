# 1. Operador and (y lógico)
# Devuelve True si ambas condiciones son verdaderas.
a = 10
b = 20

# Ambas condiciones deben ser verdaderas
print(a > 5 and b > 15)  # True (10 > 5 y 20 > 15)
print(a > 15 and b > 15) # False (10 no es mayor que 15)


# 2. Operador or (o lógico)
# Devuelve True si al menos una condición es verdadera.
a = 5
b = 8

# Basta con que una condición sea verdadera
print(a > 3 or b > 10)  # True (a > 3 es verdadero)
print(a > 6 or b > 10)  # False (ambas son falsas)



# 3. Operador not (negación lógica)
# Invierte el valor lógico de una condición: True se convierte en False y viceversa.
a = 10

# Invierte el resultado
print(not (a > 5))  # False (porque a > 5 es True)
print(not (a > 15)) # True (porque a > 15 es False)



# 4. Combinaciones de operadores lógicos
# Puedes combinar and, or, y not en expresiones más complejas. Python evalúa de acuerdo con la precedencia:
#
# Primero se evalúa not,
# Luego and,
# Y finalmente or.
# Usa paréntesis para garantizar claridad.

a = 5
b = 10
c = 15

# Expresión combinada
print(a < b and b < c or a > c)  # True (a < b < c es verdadero)
print(not (a > b or b > c))      # True (ambas condiciones son falsas)



# 5. Evaluación lógica con valores no booleanos
# En Python, cualquier valor puede usarse en una expresión lógica:
#
# Valores "falsos": 0, None, False, cadenas vacías (""), listas vacías ([]), etc.
# Valores "verdaderos": Cualquier otro valor.
# Ejemplo con `and` y `or`
x = ""
y = "Hola"
z = None

print(x or y)  # "Hola" (retorna el primer valor verdadero)
print(x and y) # "" (retorna el primer valor falso)
print(not z)   # True (porque z es None, un valor "falso")



# 6. Uso con all() y any()
# Para evaluar múltiples condiciones:
#
# all(): Retorna True si todas las condiciones son verdaderas.
# any(): Retorna True si al menos una condición es verdadera.

# Ejemplo con listas
condiciones = [5 > 3, 10 > 2, 1 > 0]

print(all(condiciones))  # True (todas las condiciones son verdaderas)
print(any(condiciones))  # True (al menos una condición es verdadera)

# Si una condición es falsa
condiciones = [5 > 3, 10 > 2, 1 < 0]
print(all(condiciones))  # False (no todas son verdaderas)




# 7. Casos avanzados
# Condicionales en expresiones compactas
# Los operadores lógicos se usan frecuentemente en expresiones ternarias o estructuras más avanzadas.
x = 15
y = 20

# Expresión compacta
mensaje = "Ambos son mayores que 10" if x > 10 and y > 10 else "Uno o ambos son menores"
print(mensaje)  # "Ambos son mayores que 10"

# Filtrado con listas por comprensión
numeros = [1, 5, 10, 15, 20]
pares_y_mayores_que_10 = [n for n in numeros if n % 2 == 0 and n > 10]

print(pares_y_mayores_que_10)  # [20]


# Orden de evaluación
# Para recordar el orden de evaluación, piensa en esta prioridad:
#
# not (primero se evalúa la negación).
# and (después las conjunciones).
# or (al final las disyunciones).









