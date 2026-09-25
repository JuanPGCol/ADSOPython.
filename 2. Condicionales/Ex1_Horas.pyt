horas = int(input("Indique la cantidad de horas laboradas: "))


#Calculo/condicion para liquidar extras
valorH = 15000
if horas>40:
    print("Se realizara el calculo de horas extras")
    print('-'*50)
    horasTotales = 40+((horas-40)*2)
    pagoTotal = horasTotales*valorH
    print("El pago es: ",pagoTotal)
    print('-'*50)
else:    
    pagoTotal = horas*valorH
    print("No aplica pago con horas extras")
    print('-'*50)
    print("El pago sera: ",pagoTotal)
    print('-'*50)