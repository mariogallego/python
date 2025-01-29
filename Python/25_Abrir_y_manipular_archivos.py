
# En Python, trabajar con archivos es una tarea común que se puede realizar utilizando las
# funciones y métodos integrados. Aquí te doy una introducción a las operaciones básicas:
#
# Abrir un archivo
# Para abrir un archivo, usamos la función open(). Su sintaxis básica es:
# archivo = open("nombre_del_archivo.txt", modo)

# El parámetro modo determina cómo queremos abrir el archivo:
#
# "r": Solo lectura (modo predeterminado).
# "w": Escritura (sobrescribe si existe, o crea uno nuevo).
# "x": Crea un archivo, pero lanza un error si ya existe.
# "a": Agregar información al final del archivo.
# "b": Modo binario (ej., imágenes).
# "t": Modo texto (predeterminado).
# "+": Lectura y escritura.

# Leer archivos
# 1. Leer todo el contenido del archivo:
with open("Prueba.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# 2. Leer línea por línea:
with open("Prueba.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # `.strip()` elimina los saltos de línea

# 3. Leer líneas como lista:
with open("Prueba.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)  # Cada línea es un elemento de la lista




# Escribir en archivos
# 1. Escribir texto:
with open("Prueba.txt", "w") as archivo:
    archivo.write("Hola, este es un texto de prueba.\n")


# 2. Agregar texto al final:
with open("Prueba.txt", "a") as archivo:
    archivo.write("Esta línea se añade al final.\n")


# Archivos binarios
# Para manejar archivos binarios, como imágenes:
#
# 1. Leer en modo binario:
with open("imagen.jpg", "rb") as archivo:
    contenido = archivo.read()
    # print(contenido)


# 2. Escribir en modo binario:
with open("nueva_imagen.jpg", "wb") as archivo:
    archivo.write(contenido)

# Cerrar archivos
# Aunque usar with cierra automáticamente el archivo,
# puedes cerrarlo manualmente con archivo.close() si no usas el bloque with.
lista = ["a","b","c","d"]
archivo = open("Prueba.txt", "a")
for num in lista:
    archivo.writelines(num + '\n')
archivo.close()

# Ejemplo completo: Copiar contenido de un archivo a otro
with open("Prueba.txt", "r") as origen:
    contenido = origen.read()

with open("archivo_destino.txt", "w") as destino:
    destino.write(contenido)







