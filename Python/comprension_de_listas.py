palabra = 'python'
lista = [letra for letra in palabra]
print(lista)
for letra in palabra:
    print(letra)


pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)