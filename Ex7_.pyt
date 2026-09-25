#Veterinaria

#Informacion de ingreso
cliente = str(input("Ingrese el nombre del paciente para la facturacion: "))
cantidad = int(input("Ingresa la cantidad de pacientes"))

#Calculos
valor = 50000*cantidad
iva = valor*0.19
total = valor+iva

#Informacion de salida
"El valor de la consulta por los",cantidad,"clientes fue: ",total