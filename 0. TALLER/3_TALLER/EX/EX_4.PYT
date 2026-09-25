numero = int(input("Indique un numero entero y positivo: "))

#calculo
calculo=1

for i in range (numero-1):
    i+=1
    
    calculo=calculo*numero
    print(f"el resultado es: {calculo}")
    numero-=1
    