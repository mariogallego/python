# Tuplas
# Las tuplas en Python son estructuras de datos similares a las listas,
# pero tienen una característica importante: son inmutables.
# Una vez creada una tupla, sus elementos no pueden modificarse (ni añadirse, ni eliminarse).
# Son ideales para representar datos que no deben cambiar durante la ejecución del programa.

# Características principales
# Inmutables: No se pueden modificar después de su creación.
# Ordenadas: Los elementos tienen un orden fijo.
# Admiten duplicados: Una tupla puede contener valores repetidos.
# Heterogéneas: Pueden almacenar cualquier tipo de dato (int, str, listas, etc.).
# Eficientes: Son más rápidas que las listas para ciertas operaciones.



# Ventajas de las tuplas
# Seguridad: Al ser inmutables, aseguran que los datos no cambien accidentalmente.
# Rendimiento: Son más rápidas que las listas para búsquedas y operaciones que no requieran modificaciones.
# Compatibilidad: Se pueden usar como claves en diccionarios (las listas no)


# Aquí tienes un ejemplo práctico de cómo usar tuplas como claves en un diccionario.
# Esto es posible porque las tuplas son inmutables y, por lo tanto, pueden ser usadas como claves
# (a diferencia de las listas, que son mutables y no pueden usarse como claves).
#
# Ejemplo: Coordenadas como claves de un diccionario
# Supongamos que queremos mapear ubicaciones específicas (representadas por coordenadas x, y) a ciertos valores, como nombres de ciudades.

# Diccionario usando tuplas como claves
ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles",
    (48.8566, 2.3522): "París",
    (35.6895, 139.6917): "Tokio"
}

# Acceder a un valor usando una tupla como clave
coordenada = (40.7128, -74.0060)
print(f"La ciudad en {coordenada} es {ubicaciones[coordenada]}")
# Salida: La ciudad en (40.7128, -74.0060) es Nueva York

# Añadir una nueva ubicación
ubicaciones[(51.5074, -0.1278)] = "Londres"

# Ver todas las ubicaciones
for coord, ciudad in ubicaciones.items():
    print(f"Coordenadas: {coord}, Ciudad: {ciudad}")
# Salida:
# Coordenadas: (40.7128, -74.0060), Ciudad: Nueva York
# Coordenadas: (34.0522, -118.2437), Ciudad: Los Ángeles
# Coordenadas: (48.8566, 2.3522), Ciudad: París
# Coordenadas: (35.6895, 139.6917), Ciudad: Tokio
# Coordenadas: (51.5074, -0.1278), Ciudad: Londres


# Otro ejemplo: Producto como clave y precio como valor
# Podemos usar una tupla para combinar un producto y su variante (por ejemplo, color y tamaño) como clave en un diccionario:
# Diccionario con tuplas como claves
productos = {
    ("camiseta", "roja", "M"): 19.99,
    ("camiseta", "azul", "L"): 21.99,
    ("pantalón", "negro", "32"): 39.99,
    ("zapatos", "blancos", "42"): 49.99
}

# Consultar el precio de un producto
clave = ("camiseta", "roja", "M")
print(f"El precio de {clave} es ${productos[clave]}")
# Salida: El precio de ('camiseta', 'roja', 'M') es $19.99

# Agregar un nuevo producto
productos[("chaqueta", "verde", "L")] = 59.99

# Mostrar todos los productos y precios
for producto, precio in productos.items():
    print(f"Producto: {producto}, Precio: ${precio}")






















