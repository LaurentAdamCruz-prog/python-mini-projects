# --- SOLICITUD DE DATOS ---
# Solicitud de datos al usuario. 
nombre_estudiante = input("Introduce tu nombre: ")
edad_estudiante = int(input("Introduce tu edad: "))
nombre_curso_estudiante = input("Introduce el nombre del curso que estas completando: ")

# Solicitamos 3 últimas evaluaciones. 
calificacion_1 = float(input("Introduce tu primera calificación 0/10: "))
calificacion_2 = float(input("Introduce tu segunda calificación 0/10: "))
calificacion_3 = float(input("Introduce tu tercera calificación 0/10: "))

# Creamos la lista vacia de las calificaciones. 
calificaciones = []

# Agregamos las calificaciones previamente introducidas a la lista "calificaciones".
calificaciones.append(calificacion_1)
calificaciones.append(calificacion_2)
calificaciones.append(calificacion_3)

# --- OPERACIONES ---

# Suma de las calificaciones. 
suma_calificaciones = sum(calificaciones)

# Calculo del promedio de las calificaciones. 
promedio_calificaciones = suma_calificaciones / len(calificaciones)

# Calculo separación entre el 10 y el promedio. 
diferencia_promedio = 10 - promedio_calificaciones

# Comparación que determina si el promedio es igual o superior a 5. (Guardamos resultado BOOL)
comparacion_promedio = promedio_calificaciones >= 5 

# --- CREACIÓN DICCIONARIO CON DATOS ---
dic_estudiante = {

    "nombre" : nombre_estudiante,
    "edad" : edad_estudiante,
    "curso" : nombre_curso_estudiante,
    "calificaciones" : calificaciones,
    "promedio" : promedio_calificaciones,
    "aprobado" : comparacion_promedio

}

# --- OPERACIONES CON DICCIONARIO ---

# Consultamos el nombre del estudiante mediante la clave. 
consulta_nombre = dic_estudiante["nombre"]

# Comprobamos si la clave "curso" existe en el diccionario "estudiante".
comprobacion_clave_curso = "curso" in dic_estudiante

# Consultamos mediante el método .get una clave inexistente. 
comprobacion_clave_inexistente = dic_estudiante.get("email", "No registrado")

# Solicitamos mediante input una cuarta calificación al usuario 
calificacion_4 = float(input("Introduce tu cuarta calificación 0/10: "))
calificaciones.append(calificacion_4)

# Comprobamos nuevamente el número de calificaciones que contiene la lista. 
longitud_lista_calificaciones_2 = len(calificaciones)

# Comprobación de la calificacion "10" dentro de lista "calificaciones"
comprobacion_10_calificaciones = 10 in calificaciones

# Volvemos a declarar suma, promediom diferencia y aprobado para que se actualice con la última calificacion.
suma_calificaciones = sum(calificaciones)
promedio_calificaciones = suma_calificaciones / len(calificaciones)
diferencia_promedio = 10 - promedio_calificaciones
comparacion_promedio = promedio_calificaciones >= 5 

# Modificación/Actualización valores diccionario sin crear variables de forma innecesaria. 
dic_estudiante["promedio"] = promedio_calificaciones
dic_estudiante["aprobado"] = comparacion_promedio

# Consultamos el promedio del estudiante en el diccionario mediante el método get.
consulta_promedio = dic_estudiante.get("promedio")

# IMPRIMIMOS EL RESULTADO.

print("--- PERFIL ACADÉMICO ---")
print("")
print(f"Estudiante: {consulta_nombre}")
print(f"Edad: {dic_estudiante["edad"]} años.")
print(f"Curso: {dic_estudiante["curso"]}")
print(f"Calificaciones: {calificaciones}")
print(f"Número de calificaciones: {longitud_lista_calificaciones_2}")
print(f"Promedio actualizado: {consulta_promedio:.2f}")
print(f"Aprobado: {comparacion_promedio}")
print(f"¿Existe la clave curso?: {comprobacion_clave_curso}")
print(f"¿Hay un 10? {comprobacion_10_calificaciones}")
print(f"Email: {comprobacion_clave_inexistente}")

# --- OPERACIÓN ADICIONAL ---
print(f"La suma de todas las calificaciones es: {suma_calificaciones}")
print(f"Diferencia entre máxima calificación (10) y el promedio: {diferencia_promedio:.2f}")
print(dic_estudiante)