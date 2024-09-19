# Deber Semana 14
#El objetivo de esta tarea es practicar el uso de funciones en Python, incluyendo parámetros,
# valores predeterminados y retorno de valores. Deberás crear un programa que calcule el
# descuento en compras en función del monto total de la compra y mostrar el monto final a .
#Función para calcular el descuento
def calcular_descuento(valor_total,porcentaje_descuento=40):
    descuento = valor_total * porcentaje_descuento / 100
    return descuento
#Función para mostrar el resultado
def muestra_resultados(monto_total,descuento):
    monto_resultado = monto_total  -descuento
    print(f'el monto total es:',monto_total)
    print("__________________________________")
    print(f'el monto descuento es:', descuento)
    print("__________________________________")
    print(f'el monto del resultante es:', monto_resultado)
    print("__________________________________")
monto_total1 = 2500
descuento1 = calcular_descuento(monto_total1)
muestra_resultados(monto_total1,descuento1)
