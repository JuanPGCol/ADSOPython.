#Veterinaria

#Informacion de ingreso
cliente = str(input("Ingrese el nombre del paciente para la facturacion: "))
nomMascota = str(input("Ingrese el nombre de la mascota: "))
especie = str(input("Ingrese la especie de su/s mascota/s (Perro o gato): "))
formaPago = str(input("Forma de pago (Efectivo | TD | TC): ")).lower
#Calculos
valor = 50000
iva = valor*0.19
total = valor+iva
total_TD_TC = (total * 0.04)+total

#Informacion de salida

print("---------------------------------------------")
print("Cliente: ",cliente)
print("Forma de pago: ",formaPago)
print("---------------------------------------------")
print("Proceso realizado a ",nomMascota," de especie ",especie," fue: ",total)
if formaPago == "td" or "tc":
    print(" Total: ",valor)
    print(" Total + IVA + 4% (Por pago con tarjeta): ",total_TD_TC)
else:
    print(" Total: ",valor)
    print(" Total + IVA: ",total)
    print("---------------------------------------------")