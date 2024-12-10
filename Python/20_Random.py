# Importar la Biblioteca
# Antes de usarla, debes importarla:
import random

# 1. Generar Números Aleatorios
# 1.1 random.random()
# Genera un número flotante aleatorio entre 0.0 (incluido) y 1.0 (excluido).

print(random.random())  # Ejemplo: 0.732532234


# 1.2 random.uniform(a, b)
# Genera un número flotante aleatorio en el rango [a, b].
print(random.uniform(10, 20))  # Ejemplo: 15.6743


# 1.3 random.randint(a, b)
# Genera un número entero aleatorio en el rango [a, b] (ambos extremos incluidos).
print(random.randint(1, 10))  # Ejemplo: 7


# 1.4 random.randrange(start, stop[, step])
# Genera un número entero aleatorio en el rango [start, stop), excluyendo el extremo superior. Se puede especificar un paso.
print(random.randrange(1, 10))       # Ejemplo: 5 (de 1 a 9)
print(random.randrange(1, 10, 2))   # Ejemplo: 7 (números impares: 1, 3, 5, ...)



# 2. Elegir Elementos Aleatorios
# 2.1 random.choice(seq)
# Selecciona un elemento aleatorio de una lista, tupla o cadena.
colores = ["rojo", "verde", "azul"]
print(random.choice(colores))  # Ejemplo: "verde"



# 2.2 random.choices(population, weights=None, k=1)
# Selecciona k elementos aleatorios de la lista con reemplazo
# (puede elegir el mismo elemento varias veces). Se puede asignar un peso a cada elemento.

# Sin pesos
print(random.choices([1, 2, 3], k=5))  # Ejemplo: [2, 3, 1, 2, 2]

# Con pesos (1 tiene mayor probabilidad)
print(random.choices([1, 2, 3], weights=[10, 1, 1], k=5))  # Ejemplo: [1, 1, 1, 3, 1]



# 2.3 random.sample(population, k)
# Selecciona k elementos únicos sin reemplazo (los elementos no se repiten).
print(random.sample([1, 2, 3, 4, 5], k=3))  # Ejemplo: [4, 1, 5]


# 2.4 random.shuffle(seq)
# Baraja una lista en su lugar, es decir, la modifica directamente.
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)  # Ejemplo: [3, 5, 1, 2, 4]





# 3. Semilla para Reproducibilidad (random.seed)
# La función random.seed() se utiliza para inicializar el generador de números aleatorios con un valor fijo.
# Esto asegura que los resultados sean reproducibles.
random.seed(42)
print(random.random())  # Siempre generará el mismo número (ejemplo: 0.639426798)





# 4. Ejemplo Completo
# Un ejemplo práctico que usa varias funciones de random:
import random

# Generar un número flotante aleatorio entre 0 y 1
print("random.random():", random.random())

# Generar un número flotante aleatorio entre 10 y 20
print("random.uniform(10, 20):", random.uniform(10, 20))

# Generar un número entero aleatorio entre 1 y 100
print("random.randint(1, 100):", random.randint(1, 100))

# Elegir un elemento aleatorio de una lista
colores = ["rojo", "verde", "azul", "amarillo"]
print("random.choice(colores):", random.choice(colores))

# Elegir 2 elementos únicos de una lista
print("random.sample(colores, k=2):", random.sample(colores, k=2))

# Barajar una lista
random.shuffle(colores)
print("random.shuffle(colores):", colores)




# 5. Generación de Datos Aleatorios Avanzados
# 5.1 Números aleatorios según una distribución
# Python ofrece varias funciones para generar números según distribuciones estadísticas específicas:
#
# random.gauss(mu, sigma): Genera un número basado en la distribución normal (Gaussiana) con media mu y desviación estándar sigma.
print(random.gauss(0, 1))  # Ejemplo: -0.35422


# random.expovariate(lambd): Genera un número según la distribución exponencial, con la tasa lambd.
print(random.expovariate(1.5))  # Ejemplo: 0.742


# random.betavariate(alpha, beta): Genera un número según la distribución Beta.
print(random.betavariate(2, 5))  # Ejemplo: 0.245


# 6. Resumen de las Principales Funciones
# Función	Descripción
# random.random()	Número flotante aleatorio entre 0.0 y 1.0.
# random.uniform(a, b)	Número flotante aleatorio entre a y b.
# random.randint(a, b)	Número entero aleatorio entre a y b (incluidos).
# random.randrange(a, b)	Número entero aleatorio entre a y b (excluye el extremo superior).
# random.choice(seq)	Elemento aleatorio de una lista o iterable.
# random.choices(pop, k)	Selección aleatoria de k elementos (con reemplazo).
# random.sample(pop, k)	Selección aleatoria de k elementos únicos (sin reemplazo).
# random.shuffle(seq)	Baraja una lista en su lugar.
# random.seed(n)	Fija la semilla para hacer reproducibles los números generados.

