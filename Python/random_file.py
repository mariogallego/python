from random import *

numRandom = randint(1,50)
numRandomFloat = round(uniform(1,50))
print(numRandom)
print(numRandomFloat)

colores=['azul','rojo','blanco']
randomColores = choice(colores)
print(randomColores)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)