# Lista inicial de productos.
productos_inicio = ["Pantalla", "Mouse", "Teclado", "Laptop", "Altavoces"]

# Le solicitamos al usuario que introduzca un nuevo producto.
producto_nuevo = input("Introduce un producto nuevo al carrito: ")

# Comprobación si el producto ya esta en la lista. 
if producto_nuevo not in productos_inicio:
    productos_inicio.append(producto_nuevo)

# Imprimimos por pantalla la lista actualizada. 
print(f"Lista actualizada: {productos_inicio}.")

# Imprimimos el número de elementos en la lista principal. 
print(f"Número de productos: {len(productos_inicio)}")

# Hacemos la comprobación si el producto indicado está en la lista.
comprobacion = "leche" in productos_inicio

# Imprimimos los resultados por pantalla. 
print(f"¿Hay leche en la lista?: {comprobacion}")