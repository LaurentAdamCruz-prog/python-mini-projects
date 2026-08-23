# Le solicitamos al usuario la información correspondiente.

ingreso_mensual = float(input("Introduce tus ingresos mensuales:"))
gasto_vivienda = float(input("Introduce tus gastos de vivienda:"))
gasto_alimentación = float(input("Introduce tus gastos de alimentación"))
gastos_transporte = float(input("Introduce tus gastos de transporte:"))
gastos_otros = float(input("Introduce otros gastos mensuales:"))

# Realizamos los calculos correspondientes para poder mostrar los resultados por pantalla.

gastos_mensuales_totales = gasto_vivienda + gasto_alimentación + gastos_transporte + gastos_otros
dinero_restante = ingreso_mensual - gastos_mensuales_totales
porcentaje_ahorro = (dinero_restante / ingreso_mensual) * 100

# Mostramos los resultados por pantalla. 

print(f"Ingresos mensuales: {ingreso_mensual:.2f} €")
print(f"Gastos totales: {gastos_mensuales_totales:.2f} €")
print(f"Ahorro mensual: {dinero_restante:.2f} €")
print(f"Porcentaje de ahorro: {porcentaje_ahorro:.2f} %")