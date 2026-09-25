numero = int(input("Indique el numero a validar: "))
contPrimo=0


for n in range (numero):
    n+=1

    if numero%n==0:
        contPrimo+=1

    print(contPrimo)
if contPrimo==2:
    print (f"El numero es primo")
else:
    print(f"El numero no es primo")