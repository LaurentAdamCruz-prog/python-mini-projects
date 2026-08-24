# Solicitamos datos al usuario.
nombre_tarea = input("Introduce el nombre de la tarea: ")
descripcion_tarea = input("Introduce una breve descripción de la tarea: ")
horas_tarea = float(input("Introduce el número estimado de horas necesarias: "))
prioridad_tarea = int(input("Introduce del 1 al 5 la prioridad de la tarea: "))
estado_tarea = input("Introduce el estado de la tarea como Pendiente o Completada: ")

# Comprobamos el estado en el input.
comprobacion_estado = estado_tarea == "Completada"

# Realizamos la fórmula para calcular los minutos correspondientes a la hora.
minutos_tarea = horas_tarea * 60

# Creamos la lista de etiquetas vacia.
etiquetas = []

# Le solicitamos al usuario que introduzca dos etiquetas. 
etiquetas_tarea = input("Introduce dos etiquetas separadas por una , relacionadas con la tarea: ")

# Separamos los elementos que estan entre ","
separacion = etiquetas_tarea.split(",")

# Limpiamos los espacios de ambos elementos str. 
etiqueta_1 = separacion[0].strip()
etiqueta_2 = separacion[1].strip()

# Agregamos ambos elementos limpios a la lista.
etiquetas.append(etiqueta_1)
etiquetas.append(etiqueta_2)

# Comprobamos si la etiqueta "Python" existe en la lista etiquetas.
"Python" in etiquetas

# Creamos el diccionario con las claves indicadas en el enunciado.
tarea = {"nombre" : nombre_tarea,
         "descripcion" : descripcion_tarea,
         "horas_estimadas" : horas_tarea,
         "minutos_estimados" : minutos_tarea,
         "prioridad" : prioridad_tarea,
         "estado" : estado_tarea,
         "completada" : comprobacion_estado,
         "etiquetas" : etiquetas
         }

# Obtenemos el nombre de la tarea consultado la primera clave del diccionario mediante su clave.
tarea["nombre"]

# Obtenemos la prioridad de la tarea consultado la clave del diccionario mediante el método .get().
tarea.get("prioridad")

# Consultamos una clave inexistente en el diccionario imprimiendo un valor personalizado por pantalla en caso False.
tarea.get("fecha_limite", "No definida")

# Consultamos si "estado" existe en el diccionario como clave.
"estado" in tarea

# Comprobamos si la etiqueta "Python" existe en la clave "etiquetas" del diccionario.
comprobacion_etiqueta = "Python" in tarea["etiquetas"]

# Le solicitamos al usuario que introduzca una nueva etiqueta para la tarea. 
nueva_etiqueta = input("Introduce una nueva etiqueta para la tarea: ")

etiqueta_3 = nueva_etiqueta.strip() 

# Agregamos la etiqueta recientemente introducida a la lista de la clave "etiquetas" en el diccionario. 
tarea["etiquetas"].append(etiqueta_3)

# Consultamos en número de elementos que contiene la lista "etiquetas" dentro del diccionario.
num_etiquetas_dic = len(tarea["etiquetas"])

# Resultado impreso por pantalla.
print("--- RESUMEN DE LA TAREA ---")
print("")
print(f"Tarea: {tarea["nombre"]}")
print(f"Descripción: {tarea["descripcion"]}")
print(f"Prioridad: {tarea["prioridad"]}")
print(f"Horas estimadas: {tarea["horas_estimadas"]}")
print(f"Minutos estimados: {tarea["minutos_estimados"]:.2f}")
print(f"Estado: {tarea["estado"]}")
print(f"Completada: {tarea["completada"]}")
print(f"Etiquetas: {tarea["etiquetas"]}")
print(f"Número de etiquetas: {len(tarea["etiquetas"])}")
print(f"Contiene la etiqueta Python: {"Python" in tarea["etiquetas"]}")
print(f"Fecha límite: {tarea.get("fecha_limite", "No definida")}")

