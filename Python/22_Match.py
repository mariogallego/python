serie = 1

match serie:
    case 1|10:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)


cliente = {'nombre':'fede', 'edad':45, 'ciudad':'leon'}

for e in cliente.values():
    match e:
        case 'alberto':
            print(e)
        case 'fede':
            print(e)




def evaluar_numero(numero):
    match numero:
        case n if n > 0:
            return "Número positivo"
        case n if n < 0:
            return "Número negativo"
        case _:
            return "Es cero"

print(evaluar_numero(5))   # Salida: Número positivo
print(evaluar_numero(-3))  # Salida: Número negativo
print(evaluar_numero(0))   # Salida: Es cero


# Desempaquetado en patrones (estructuras anidadas):
# match-case también funciona con estructuras como listas, tuplas y diccionarios.
#
# Listas o tuplas:
def identificar_estructura(estructura):
    match estructura:
        case [x, y]:  # Coincide si es una lista/tupla de 2 elementos
            return f"Lista o tupla con 2 elementos: {x}, {y}"
        case [x, y, z]:
            return f"Lista o tupla con 3 elementos: {x}, {y}, {z}"
        case _:
            return "Estructura desconocida"

print(identificar_estructura([1, 2]))       # Salida: Lista o tupla con 2 elementos: 1, 2
print(identificar_estructura((1, 2, 3)))   # Salida: Lista o tupla con 3 elementos: 1, 2, 3
print(identificar_estructura([1, 2, 3, 4]))  # Salida: Estructura desconocida


# Diccionarios
def procesar_diccionario(d):
    match d:
        case {"nombre": nombre, "edad": edad}:
            return f"Nombre: {nombre}, Edad: {edad}"
        case _:
            return "Diccionario no coincide con el patrón"

print(procesar_diccionario({"nombre": "Ana", "edad": 30}))  # Salida: Nombre: Ana, Edad: 30
print(procesar_diccionario({"apellido": "Lopez"}))          # Salida: Diccionario no coincide con el patrón

#
cliente = {'nombre':'fede', 'edad':45, 'ciudad':'leon'}
pelicula = {'titulo':'matrix', 'year':1999}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {
            'nombre': nombre,
            'edad': edad,
            'ciudad': ciudad
        }:
            print (nombre, edad, ciudad)
        case {
            'titulo': titulo,
            'year': year
        }:
            print(titulo, year)
        case _:
            print('no idea')