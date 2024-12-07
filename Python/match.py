serie = 1

match serie:
    case 1:
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

pelicula = {'titulo':'matrix', 'año':1999}

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
            'año': año
        }:
            print(titulo, año)
        case _:
            print('no idea')