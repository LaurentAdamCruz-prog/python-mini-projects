# Solicitamos información del producto al usuario. 

nombre_producto = input("Introduce el nombre del producto: ")
categoria_producto = input("Introduce la categoría del producto: ")
precio_unitario = float(input("Agrega el precio unitario: "))
cantidad_actual_producto = int(input("Ingresa las PZS disponibles en stock: "))
cantidad_minima_producto = int(input("Ingresa las PZS mínimas a mantener en inv: "))

# Calculamos el valor del inventario multplicando el precio unitario por la cantidad en PZS.
valor_stock_producto = precio_unitario * cantidad_actual_producto

# Verificamos mediante una formúla de comparación si la cantidad actual es inferior o superior a la cantidad mínima
comprobacion_stock_bajo = cantidad_actual_producto < cantidad_minima_producto

# Creamos una lista de etiquetas vacía. 
etiquetas = []

# Le solicitamos al usuario que introduzca dos etiquetas y realizamos las operaciones correspondientes para separar los elementos y eliminar los espacios. 
creacion_etiquetas = input("Introduce dos etiquetas separadas por una coma: ")
creacion_etiquetas_separacion = creacion_etiquetas.split(",")
creacion_etiquetas_espacios_0 = creacion_etiquetas_separacion[0].strip()
creacion_etiquetas_espacios_1 = creacion_etiquetas_separacion[1].strip()
etiquetas.append(creacion_etiquetas_espacios_0)
etiquetas.append(creacion_etiquetas_espacios_1)

# Creamos el diccionario producto con las claves:valor de cada uno de los elementos.
producto = {
    "nombre" : nombre_producto,
    "categoria" : categoria_producto,
    "precio" : precio_unitario,
    "cantidad" : cantidad_actual_producto,
    "stock_minimo" : cantidad_minima_producto,
    "valor_stock" : valor_stock_producto,
    "stock_bajo" : comprobacion_stock_bajo,
    "etiquetas" : etiquetas
}

# Obtenemos el nombre del producto mediante el método get.
nombre_dic = producto.get("nombre")

# Comprobamos si la clave "cantidad" existe en el diccionario "producto".
comprobacion_dic = "cantidad" in producto

# Buscamos la clave "proveedor" en el diccionario "producto" si no la obtenemos asignamos un valor por defecto.
comprobacion_dic_2 = producto.get("proveedor", "No asignado")

# Comprobamos la cantidad de "claves:valor" en el diccionario producto.
num_claves_dic = len(producto)

# Le solicitamos al usuario que introduzca una tercera etiqueta y la agregamos a la lista "etiquetas".
solicitud_etiqueta = input("Introduce una tercera etiqueta para el producto: ")
solicitud_etiqueta_espacio = solicitud_etiqueta.strip()
etiquetas.append(solicitud_etiqueta_espacio)

# Comprobamos si la etiqueta "Tecnología" existe en la lista de etiquetas
comprobacion_etiqueta = "Tecnología" in etiquetas

# Comprobamos la cantidad de elementos en la lista "etiquetas".
num_etiquetas = len(etiquetas)

# Imprimimos el resultado.
print("--- INVENTARIO ---")
print("")
print(f"Producto: {producto["nombre"]}")
print(f"Categoría: {producto["categoria"]}")
print(f"Precio unitario: {producto["precio"]:.2f} €")
print(f"Cantidad disponible: {producto["cantidad"]} PZS")
print(f"Valor total del stock: {producto["valor_stock"]:.2f} €")
print(f"Stock mínimo: {producto["stock_minimo"]} PZS")
print(f"¿Stock bajo?: {producto["stock_bajo"]}")
print(f"Etiquetas: {producto["etiquetas"]}")
print(f"Número de etiquetas: {num_etiquetas}")
print(f"Proveedor: {comprobacion_dic_2}")
print("")
print("--- COMPROBACIONES TECNICAS ---")
print(f"¿Existe la clave cantidad en el diccionario? {comprobacion_dic}")
print(f"¿Cuántos elementos contiene el diccionario producto? {num_claves_dic}")
print(f"¿Existe la clave Tecnología en la lista etiquetas? {comprobacion_etiqueta}")