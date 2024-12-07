#Substring
# 1. Extraer una Substring usando Slicing ([inicio:fin])
# cadena[inicio:fin:paso]
# inicio (opcional): Índice desde donde comienza la substring (inclusivo).
# fin (opcional): Índice donde termina la substring (exclusivo).
# paso (opcional): Cuántos pasos saltar (por defecto, 1).

cadena = "Hola mundo"

# Substring de los primeros 4 caracteres
print(cadena[0:4])  # Resultado: 'Hola'

# Substring desde el índice 5 hasta el final
print(cadena[5:])  # Resultado: 'mundo'

# Substring desde el principio hasta el índice 4 (exclusivo)
print(cadena[:4])  # Resultado: 'Hola'

# Substring con salto de caracteres
print(cadena[0:9:2])  # Resultado: 'Hl ud'

# Substring inversa
print(cadena[::-1])  # Resultado: 'odnum aloH' (invierte la cadena)



# 2. Buscar una Substring

# in
# Verifica si una substring está contenida en la cadena.
cadena = "Hola mundo"
print("mundo" in cadena)  # Resultado: True
print("Python" in cadena)  # Resultado: False

# index
# Similar a find(), pero lanza un error (ValueError) si la substring no se encuentra.
print(cadena.index("mundo"))  # Resultado: 5
# print(cadena.index("Python"))  # Lanza: ValueError

# count
# Devuelve el número de veces que una substring aparece en la cadena.
cadena = "Hola mundo, mundo cruel"
print(cadena.count("mundo"))  # Resultado: 2



# 3. Manipular Substrings

# Reemplazar una Substring (replace())
cadena = "Hola mundo"
print(cadena.replace("mundo", "Python"))  # Resultado: 'Hola Python'


# Dividir una Cadena en Substrings (split())
cadena = "Hola mundo, bienvenido a Python"
print(cadena.split())  # Resultado: ['Hola', 'mundo,', 'bienvenido', 'a', 'Python']

# Dividir por una substring específica
print(cadena.split("mundo"))  # Resultado: ['Hola ', ', bienvenido a Python']


# Unir Substrings (join())
lista = ["Hola", "mundo", "Python"]
print(" ".join(lista))  # Resultado: 'Hola mundo Python'


# 4. Comparar substrings
cadena = "Hola mundo"
substring = cadena[0:4]

print(substring == "Hola")  # Resultado: True
print(substring != "Mundo")  # Resultado: True



# 5. Substring con Expresiones Regulares (re)
# Si necesitas buscar patrones complejos de substrings, puedes usar el módulo re.
import re

cadena = "Hola mundo, bienvenido a Python"
# Buscar una palabra
resultado = re.search("mundo", cadena)
if resultado:
    print(f"Encontrado en el índice: {resultado.start()}")  # Resultado: 5























