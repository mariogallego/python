#Cast

#Conversion Implicita
# Conversión de entero a flotante
x = 10
y = 3.14
resultado = x + y  # Python convierte automáticamente x a flotante
print(resultado)  # 13.14
print(type(resultado))  # <class 'float'>



#Conversion Explicita
# 1. De cadena a número (y viceversa):
# Ejemplo de cadena a entero
print("De cadena a número (y viceversa):")
num = int("42")  # Resultado: 42
print(type(num))  # <class 'int'>

# entero a cadena
cadena = str(42)  # Resultado: "42"
print(type(cadena))  # <class 'str'>

# float a cadena
cadenaFloat = str(2.5)
print(type(cadenaFloat))

# float a cadena
cadenaFloat = str(2.5)
print(type(cadenaFloat))

# cadena a float
floatNum = float("2.5")
print(type(floatNum))

print("--------------------------------")

# 2. De número a booleano:
print("De número a booleano:")
print(bool(0))    # False
print(bool(1))    # True
print(bool(-5))   # True

print("--------------------------------")

# 3. De lista, tupla, y conjunto, y viceversa.
tupla = (1, 2, 3)
lista = list(tupla)  # [1, 2, 3]
print(type(lista))  # <class 'list'>

conjunto = set(lista)  # {1, 2, 3}
print(type(conjunto))  # <class 'set'>

print(type(tuple([4,5,6])))


# 4. De cadena a lista o viceversa
# list() para convertir una cadena en una lista de caracteres.
# join() para convertir una lista de cadenas en una sola cadena.

print("4. De cadena a lista o viceversa")
# De cadena a lista
palabra = "hola"
lista_caracteres = list(palabra)  # ['h', 'o', 'l', 'a']
print(lista_caracteres)

# De lista a cadena
lista = ['h', 'o', 'l', 'a']
cadena = ''.join(lista)  # "hola"
print(cadena)

print("5. De lista a dic")
diccionario_desde_lista = dict([("clave1", "valor1"), ("clave2", "valor2")])
print(diccionario_desde_lista)
# Resultado: {'clave1': 'valor1', 'clave2': 'valor2'}



# De objeto a diccionario (para clases personalizadas), dic()
##Errores en el casting
# int("42a")  # Error: ValueError
# float("abc")  # Error: ValueError















