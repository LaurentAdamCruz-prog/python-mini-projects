# Creamos el diccionario principal con valores por defecto. 
usuario = {"nombre" : "Laurent",
           "edad" : 23,
           "ciudad" : "Shanghai",
           "profesion" : "Programador"}

# Imprimimos los resultados del diccionario inicial por pantalla. 
print(f"El perfil de usuario: {usuario}.")

# Imprimimos solo el nombre por pantalla del diccionario principal.
print(f"El nombre del usuario es: {usuario["nombre"]}.")

# Imprimimos sol la ciudad con el método get. 
print(f"La ciudad del usuario es: {usuario.get("ciudad")}")

# Consultamos una clave que no existe con el método .get
print(f"Comprobación de clave: {usuario.get("telefono", "No disponible")}")

# Le solicitamos al usuario que introduzca su nueva ciudad. 
nueva_profesion = input("Introduce tu nueva profesión: ")

# Actualizamos la clave "ciudad" del diccionario principal.
usuario["profesion"] = nueva_profesion

# Mostramos el diccionario actualizado por pantalla. 
print(usuario)

# Realizamos la comprobación de la clave "email" dentro de usuario. 
comprobacion_clave = "email" in usuario

# Imprimimos los resultados por pantalla.
print(f"¿Existe la clave email en el diccionario usuario: {comprobacion_clave}.")

# Comprobación de cuantos elementos tiene el diccionario usuario.
print(f"El diccionario cuenta con: {len(usuario)} elementos.")