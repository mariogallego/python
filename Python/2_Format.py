# Format

# En Python, el metodo format se utiliza para formatear cadenas de texto de una manera flexible y legible.
# Este metodo permite insertar valores dentro de cadenas de texto mediante marcadores de posición.

# Reemplazo simple
print("Hola, {}!".format("Mundo"))  # Hola, Mundo!

# Múltiples marcadores
print("Soy {} y tengo {} años.".format("Juan", 25))  # Soy Juan y tengo 25 años.

# Reordenamiento con índices
print("{1} es más grande que {0}".format(3, 5))  # 5 es más grande que 3


persona = "Juan"
edad = 30
print("Me llamo {nombre} y tengo {edad} años.".format(nombre=persona, edad=edad))


#format avanzado
#Alineación izquierda, derecha y centrada:
print("{:<10}".format("izq"))   # 'izq       ' (izquierda)
print("{:>10}".format("der"))   # '       der' (derecha)
print("{:^10}".format("centro"))  # '  centro  ' (centrado)

#Números con ceros al inicio:
print("{:05}".format(42))  # '00042'

#Redondeo de números
print("{:.2f}".format(3.14159))  # '3.14' (2 decimales)

#Agregar separación de miles:
print("{:,}".format(10000000))  # '1,000,000'


#F-Strings
nombre = "Ana"
edad = 28
print(f"Hola, soy {nombre} y tengo {edad} años.")  # Hola, soy Ana y tengo 28 años.













