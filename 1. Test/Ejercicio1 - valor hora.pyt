#Solicitud
horasLab = input("Indique la cantidad de horas laboradas: ")
valorHora = input("Indique el valor de la hora: ")
print("-----------------")

#Calculos
salarioTotal =float(horasLab)*float(valorHora)
descuento = float(salarioTotal)*0.12
salarioDesc =(salarioTotal)-(descuento)

#POV
print("El salario total es: ",salarioTotal)
print("El valor del descuento es: ",descuento)
print("-----------------")
print("El salario a consignar es: ",salarioDesc)
print("-----------------")