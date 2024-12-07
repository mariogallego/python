
# 1. Los strings son inmutables
cadena = "Hola"
# Intentar modificar un carácter dará un error
# cadena[0] = "M"  # Esto genera un TypeError

# Solución: debes crear una nueva cadena
cadena = "M" + cadena[1:]
print(cadena)  # Resultado: 'Mola'



# 2. Los strings son secuencias ordenadas
cadena = "Python"

# Acceso por índice
print(cadena[0])   # Resultado: 'P'
print(cadena[-1])  # Resultado: 'n' (índice inverso)

# Slicing
print(cadena[0:3])  # Resultado: 'Pyt' (de índice 0 a 2)
print(cadena[::-1]) # Resultado: 'nohtyP' (cadena invertida)



# 3. Los strings son iterables
cadena = "Hola"
for caracter in cadena:
    print(caracter)
# Resultado:
# H
# o
# l
# a



# 4. Los strings pueden ser de cualquier longitud
cadena_larga = "a" * 1000  # Crea una cadena de 1000 caracteres 'a'
print(len(cadena_larga))   # Resultado: 1000



# 5. Los strings admiten concatenación y repetición
# Concatenación
saludo = "Hola" + " Mundo"
print(saludo)  # Resultado: 'Hola Mundo'

# Repetición
repetido = "Hola " * 3
print(repetido)  # Resultado: 'Hola Hola Hola '




# 6. Los strings son comparables
print("abc" == "abc")  # Resultado: True
print("abc" < "abd")   # Resultado: True (por orden alfabético)
print("Python" > "Java")  # Resultado: True (P está después de J)




# 7. Soportan operadores de membresía (in y not in)

cadena = "Hola Mundo"
print("Mundo" in cadena)      # Resultado: True
print("Python" not in cadena) # Resultado: True



# 8. Los strings admiten formateo
nombre = "Juan"
edad = 30

# Usando format
print("Hola, me llamo {} y tengo {} años".format(nombre, edad))
# Resultado: 'Hola, me llamo Juan y tengo 30 años'

# Usando f-strings (Python 3.6+)
print(f"Hola, me llamo {nombre} y tengo {edad} años")
# Resultado: 'Hola, me llamo Juan y tengo 30 años'




# 9. Son compatibles con métodos avanzados (regex)
import re

cadena = "Hola, mi número es 123-456-7890"
resultado = re.search(r"\d{3}-\d{3}-\d{4}", cadena)
if resultado:
    print("Número encontrado:", resultado.group())
# Resultado: 'Número encontrado: 123-456-7890'



# 10. Pueden contener cualquier carácter Unicode
cadena = "Python es 💻 y 🐍"
print(cadena)  # Resultado: 'Python es 💻 y 🐍'










