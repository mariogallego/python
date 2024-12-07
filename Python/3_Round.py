# Round
# Redondear al entero más cercano
print(round(3.14159))      # Resultado: 3

# Redondear con decimales
print(round(3.14159, 2))  # Resultado: 3.14

# Redondear números negativos
print(round(-2.718, 1))   # Resultado: -2.7


# Redondeo hacia abajo o hacia arriba
import math
print(math.floor(3.7))  # Resultado: 3
print(math.floor(-2.1)) # Resultado: -3

print(math.ceil(3.2))  # Resultado: 4
print(math.ceil(-2.8)) # Resultado: -2


# Redondeo hacia cero
print(int(3.9))   # Resultado: 3
print(int(-3.9))  # Resultado: -3


# Usando decimal para mayor precisión
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN

# Crear un número decimal
numero = Decimal('3.14159')

# Redondear hacia el entero más cercano
print(numero.quantize(Decimal('1'), rounding=ROUND_HALF_UP))  # Resultado: 3

# Redondear con precisión de 2 decimales
print(numero.quantize(Decimal('0.01'), rounding=ROUND_DOWN))  # Resultado: 3.14



















