
# 1.Keys
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
claves = mi_diccionario.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])

# Puedes convertirlo en una lista
print(list(claves))  # Salida: ['nombre', 'edad', 'ciudad']



# 2.Values
valores = mi_diccionario.values()
print(valores)  # Salida: dict_values(['Juan', 30, 'Madrid'])

# Convertir a lista
print(list(valores))  # Salida: ['Juan', 30, 'Madrid']



# 3.Items
pares = mi_diccionario.items()
print(pares)  # Salida: dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])

# Iterar sobre los pares clave-valor
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
# Salida:
# nombre: Juan
# edad: 30
# ciudad: Madrid



#4. get(clave, valor_predeterminado)
print(mi_diccionario.get("edad"))  # Salida: 30
print(mi_diccionario.get("profesion", "No especificado"))  # Salida: No especificado






# 5. pop(clave, valor_predeterminado)
# Elimina una clave del diccionario y devuelve su valor.
# Si la clave no existe, devuelve el valor predeterminado (opcional).
edad = mi_diccionario.pop("edad")
print(edad)  # Salida: 30
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'ciudad': 'Madrid'}

# Usando un valor predeterminado
profesion = mi_diccionario.pop("profesion", "Desconocido")
print(profesion)  # Salida: Desconocido



# 6. update(otro_diccionario)
# Actualiza el diccionario con los pares clave-valor de otro diccionario.
nuevo_diccionario = {"pais": "España", "edad": 31}
mi_diccionario.update(nuevo_diccionario)
print(mi_diccionario)
# Salida: {'nombre': 'Juan', 'ciudad': 'Madrid', 'pais': 'España', 'edad': 31}


# 7. clear()
# Elimina todos los elementos del diccionario.
mi_diccionario.clear()
print(mi_diccionario)  # Salida: {}




# 8. copy()
# Devuelve una copia superficial del diccionario.
mi_diccionario = {"nombre": "Juan", "edad": 30}
copia = mi_diccionario.copy()
print(copia)  # Salida: {'nombre': 'Juan', 'edad': 30}

# Modificar la copia no afecta el original
copia["edad"] = 25
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 30}
print(copia)  # Salida: {'nombre': 'Juan', 'edad': 25}



#9. setdefault(clave, valor_predeterminado)
# Devuelve el valor de una clave, y si no existe, la añade con el valor predeterminado.
mi_diccionario = {"nombre": "Juan"}
print(mi_diccionario.setdefault("edad", 30))  # Salida: 30
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 30}

# Si la clave ya existe
print(mi_diccionario.setdefault("nombre", "Pedro"))  # Salida: Juan
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 30}



# 10. fromkeys(iterable, valor_por_defecto)
# Crea un nuevo diccionario con claves del iterable y un valor por defecto.
claves = ["nombre", "edad", "ciudad"]
nuevo_diccionario = dict.fromkeys(claves, "desconocido")
print(nuevo_diccionario)
# Salida: {'nombre': 'desconocido', 'edad': 'desconocido', 'ciudad': 'desconocido'}















































