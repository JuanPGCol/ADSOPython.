#Datos de arranque
digito = int(input("Indique un numero de 2(dos) digitos: "))

#Calculo
decenas = int(digito/10)
unidades = int(digito-(decenas*10))

#Informacion final
print("El numero indicado cuenta con: ")
print("Decenas: ",decenas)
print("unidades: ",unidades)