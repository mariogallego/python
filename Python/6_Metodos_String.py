# Metodos String

# 1. Métodos para Modificar Cadenas
cadena = "   Hola Mundo!   "

# Convertir a minúsculas
print(cadena.lower())          # '   hola mundo!   '

# Convertir a mayúsculas
print(cadena.upper())          # '   HOLA MUNDO!   '

# Primera letra en mayúscula
print(cadena.capitalize())     # '   hola mundo!   '

# Primer carácter de cada palabra en mayúscula
print(cadena.title())          # '   Hola Mundo!   '

# Invertir mayúsculas y minúsculas
print(cadena.swapcase())       # '   hOLA mUNDO!   '

# Eliminar espacios alrededor
print(cadena.strip())          # 'Hola Mundo!'

# Eliminar espacios al inicio
print(cadena.lstrip())         # 'Hola Mundo!   '

# Eliminar espacios al final
print(cadena.rstrip())         # '   Hola Mundo!'

# Reemplazar texto
print(cadena.replace("Mundo", "Python"))  # '   Hola Python!   '




# 2. Métodos para Buscar y Consultar
cadena = "Hola Mundo, bienvenido al Mundo de Python"

# Buscar el índice de la primera aparición
print(cadena.find("Mundo"))       # 5

# Buscar desde el final
print(cadena.rfind("Mundo"))      # 27

# Índice de la primera aparición (lanza error si no encuentra)
print(cadena.index("Mundo"))      # 5

# Índice desde el final (lanza error si no encuentra)
print(cadena.rindex("Mundo"))     # 27

# Contar apariciones de una subcadena
print(cadena.count("Mundo"))      # 2

# Verificar si comienza con un prefijo
print(cadena.startswith("Hola"))  # True

# Verificar si termina con un sufijo
print(cadena.endswith("Python"))  # True



# 3. Métodos para Análisis
cadena = "Hola123"

# ¿Todos los caracteres son alfanuméricos?
print(cadena.isalnum())           # True

# ¿Todos los caracteres son letras?
print(cadena.isalpha())           # False

# ¿Todos los caracteres son números?
print(cadena.isdigit())           # False

# ¿Todos los caracteres están en minúscula?
print(cadena.islower())           # False

# ¿Todos los caracteres están en mayúscula?
print(cadena.isupper())           # False

# ¿Todos los caracteres son espacios en blanco?
print("   ".isspace())            # True

# ¿Tiene formato de título (cada palabra con mayúscula)?
print(cadena.istitle())           # True



# 4. Métodos para Dividir y Unir
cadena = "Hola Mundo Bienvenido a Python"

# Dividir en palabras
print(cadena.split())             # ['Hola', 'Mundo', 'Bienvenido', 'a', 'Python']

# Dividir con un separador específico
print(cadena.split("Mundo"))      # ['Hola ', ' Bienvenido a Python']

# Dividir desde el final
print("a,b,c".rsplit(",", 1))     # ['a,b', 'c']

# Dividir por líneas
print("Hola\nMundo".splitlines()) # ['Hola', 'Mundo']

# Unir elementos con un separador
lista = ["Hola", "Mundo", "Python"]
print(" ".join(lista))            # 'Hola Mundo Python'



# 5. Métodos para Formatear
cadena = "Hola"

# Centrar con espacios
print(cadena.center(10))          # '   Hola   '

# Alinear a la izquierda
print(cadena.ljust(10))           # 'Hola      '

# Alinear a la derecha
print(cadena.rjust(10))           # '      Hola'

# Rellenar con ceros
print(cadena.zfill(10))           # '000000Hola'

# Formatear texto
print("Hola {}, bienvenido a {}".format("Juan", "Python"))
# 'Hola Juan, bienvenido a Python'








