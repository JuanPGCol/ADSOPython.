anio = int(input("Indique el año a validar: "))

#Validacion bisisesto
if anio %4 == 0 and anio %100 != 0 or anio %100 == 0:
    print ("El año es bisiesto")
else:
    print("El año no es bisiesto")