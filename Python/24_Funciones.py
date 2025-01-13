# En Python, una función es un bloque de código reutilizable que realiza una tarea específica.
# Las funciones permiten estructurar y organizar el código para hacerlo más limpio, legible y modular.

# Declarar una función
# Se utiliza la palabra clave def para definir una función:
def nombre_funcion(parametros):
    """
    Documentación de la función (opcional)
    """
    # Código de la función
    # return valor  # (Opcional) Devuelve un valor


def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Carlos")  # Salida: Hola, Carlos!


# Parámetros y argumentos
# Las funciones pueden recibir parámetros (valores que se pasan a la función) y devolver resultados.
#
# 1. Función con parámetros
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado)  # Salida: 8


# 2. Parámetros opcionales (valores por defecto)
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}!")

saludar()         # Salida: Hola, invitado!
saludar("Ana")    # Salida: Hola, Ana!


# 3. Número variable de argumentos
# *args: Recoge múltiples argumentos como una tupla.
# **kwargs: Recoge argumentos nombrados como un diccionario.
def mostrar_args(*args):
    print(args)

mostrar_args(1, 2, 3)  # Salida: (1, 2, 3)

def mostrar_kwargs(**kwargs):
    for clave, valor in kwargs.items():
        print(f"clave: {clave}, valor: {valor}")
    #print(kwargs)

mostrar_kwargs(nombre="Carlos", edad=30)  # Salida: {'nombre': 'Carlos', 'edad': 30}


# Función con retorno
# Las funciones pueden devolver valores usando la palabra clave return.
def cuadrado(x):
    return x ** 2

resultado = cuadrado(4)
print(resultado)  # Salida: 16


# Documentar una función
# Puedes añadir una cadena de documentación (docstring) al inicio de una función para explicar lo que hace.
def sumar(a, b):
    """
    Suma dos números.

    Parámetros:
    a (int): El primer número.
    b (int): El segundo número.

    Retorna:
    int: La suma de los dos números.
    """
    return a + b

help(sumar)  # Muestra la documentación
print(sumar(1,2))




# Funciones Lambda (Funciones anónimas)
# Las funciones lambda son funciones pequeñas y sin nombre, útiles para operaciones simples.
# Función lambda para sumar dos números
suma = lambda a, b: a + b
print(suma(3, 5))  # Salida: 8



# Funciones anidadas
# Puedes definir funciones dentro de otras funciones.
def funcion_externa(x):
    def funcion_interna(y):
        print(f"Solucion: {y**2}")
        return y ** 2
    return funcion_interna(x) + 10

print(funcion_externa(3))  # Salida: 19



# Funciones como argumentos
# En Python, las funciones son ciudadanos de primera clase,
# lo que significa que pueden pasarse como argumentos o devolverse como resultado.

def aplicar_operacion(func, x, y):
    return func(x, y)

resultado = aplicar_operacion(lambda a, b: a * b, 3, 5)
print(resultado)  # Salida: 15




# Ejemplo completo: Calculadora
def calculadora(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        return a / b
    else:
        return "Operación no válida"

print(calculadora(10, 5, "suma"))           # Salida: 15
print(calculadora(10, 5, "multiplicacion")) # Salida: 50
print(calculadora(10, 5, "potencia"))       # Salida: Operación no válida

# Ventajas de usar funciones:
# Reutilización de código: Reduce duplicidad y mejora la legibilidad.
# Modularidad: El código se organiza en bloques más pequeños y fáciles de mantener.
# Flexibilidad: Permite trabajar con parámetros, valores predeterminados y funciones anidadas.
# Si necesitas ejemplos más avanzados o tienes dudas específicas, ¡avísame!



# ejemplo args y kargs

args = [1,2,3,4]
kargs = {'x':1,'y':2,'z':3}

def muestra_args_kargs(*args, **kargs):
    print("**********")
    print(args)
    print(kargs)

muestra_args_kargs(args,kargs)
muestra_args_kargs(*args,**kargs)





















