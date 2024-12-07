# 1. Sentencias Condicionales
# Las sentencias condicionales permiten ejecutar un bloque de código dependiendo de si una condición es verdadera.
#
# 1.1. if
# Ejecuta un bloque de código si la condición es verdadera.
x = 10
if x > 5:
    print("x es mayor que 5")


# 1.2. if-else
# Ejecuta un bloque si la condición es verdadera, y otro bloque si es falsa.
x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5")


# 1.3. if-elif-else
# Permite evaluar múltiples condiciones.
x = 10
if x > 15:
    print("x es mayor que 15")
elif x > 5:
    print("x está entre 6 y 15")
else:
    print("x es menor o igual a 5")



# 1.4. Condicional en una sola línea
# Ideal para expresiones cortas.
x = 10
print("Mayor" if x > 5 else "Menor o Igual")



# SENTENCIAS DE CONTROL AVANZADO

# 1. Condiciones Anidadas
# Puedes anidar múltiples condiciones con if, elif, y else.
# Sin embargo, recuerda que demasiada anidación puede hacer el código difícil de leer, así que úsala con cuidado.
edad = 25
ingresos = 50000

if edad > 18:
    if ingresos > 30000:
        print("Eres un adulto con ingresos altos")
    else:
        print("Eres un adulto con ingresos bajos")
else:
    print("Eres menor de edad")



# 2. Expresiones Ternarias
# Las expresiones ternarias permiten escribir condiciones simples en una sola línea.
# Sintaxis: valor_si_true if condicion else valor_si_false
x = 10
y = 5

mayor = x if x > y else y
print(f"El mayor es: {mayor}")  # Salida: El mayor es: 10

# Ejemplo con múltiples condiciones:
edad = 20
estado = "Adulto" if edad >= 18 else "Menor"
print(estado)  # Salida: Adulto



# 3. Condicionales con all() y any()
# Las funciones all() y any() son útiles para evaluar múltiples condiciones de forma compacta.
# Evaluar si todas las condiciones son verdaderas
x = 10
y = 20
z = 30
if all([x > 5, y > 15, z > 25]):
    print("Todas las condiciones son verdaderas")

# Evaluar si al menos una condición es verdadera
if any([x > 15, y > 25, z > 15]):
    print("Al menos una condición es verdadera")




# 4. Comparaciones Múltiples en una Línea
# Python permite encadenar comparaciones, haciéndolas más legibles.
x = 15
if 10 < x < 20:  # Equivalente a (10 < x) and (x < 20)
    print("x está entre 10 y 20")


# 5. Condiciones con Colecciones
# Puedes usar estructuras como listas, tuplas, conjuntos o diccionarios directamente en las condiciones.
#
# 5.1. Verificar pertenencia (in)
colores = ["rojo", "verde", "azul"]
color = "verde"

if color in colores:
    print(f"El color {color} está en la lista")
else:
    print(f"El color {color} no está en la lista")


# 5.2. Comprobación en diccionarios












