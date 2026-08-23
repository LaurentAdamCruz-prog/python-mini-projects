# Le solicitamos al usuario el resultado sobre 4 evaluaciónes.

evaluacion_1 = float(input("Introduce calificación 1:"))
evaluacion_2 = float(input("Introduce calificación 2:"))
evaluacion_3 = float(input("Introduce calificación 3:"))
evaluacion_4 = float(input("Introduce calificación 4:"))

# Realizamos las operaciones correspondientes para poder mostrar los resultados por pantalla. 

suma_total_notas = evaluacion_1 + evaluacion_2 + evaluacion_3 + evaluacion_4
promedio_evaluaciones = suma_total_notas / 4
distancia = 10 - promedio_evaluaciones

# Imprimimos los resultados por pantalla. 

print(f"Suma de las notas: {suma_total_notas:.2f} puntos.")
print(f"Promedio: {promedio_evaluaciones:.2f} /10.")
print(f"Distancia respecto a la nota máxima: {distancia:.2f} puntos.")