#if
from random import random

if 1==1:
    print("iguales")
    if 2==2:
        print("comparar 2")
elif 1!=2:
    print("distintos")
else:
    print("else")


#for
listaFor=[1,2,3]
for num in listaFor:
    print(num)

palabra='python'
for letra in palabra:
    print(letra)

mi_dic_1 = {'nombre':'karen', 'apellido':'jurgens', 'edad':35, 'ocupacion':'Periodista'}
for item in mi_dic_1:
    print(item)

for item in mi_dic_1.items():
    print(item)

for item in mi_dic_1.keys():
    print(item)

for item in mi_dic_1.values():
    print(item)

print("********")
for a,b in mi_dic_1.items():
    print(a,b)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for num in lista_numeros:
    if(num%2==0):
        suma_pares+=num
    else:
        suma_impares+=num

print(suma_pares)


#while

#range
for num in range(1,5):
    print(num)

for num in range(5, 15, 2):
    print(num)

lista = list(range(0,100,2))
print(lista)


#enumerator
listaIndex = ['a','b','c']
for indice,item in enumerate(listaIndex):
    print(indice,item)

#zip
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [1,2,3]
ciudades = ['a','b','c']
listaZip = list(zip(nombres,edades, ciudades))
print(listaZip)
for nombre,edad, ciudad in listaZip:
    print(nombre, edad, ciudad)


#min max
print(min(5,7,1))
print(max(5,7,1))






















