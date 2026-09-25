num1 = int(input("Indique en primer digito: "))
num2 = int(input("Indique el segundo digito: "))
num3 = int(input("Indique el tercer digito: "))
print('-'*50)

#Validacion de numero mayor
if num1>num2:
    if num1>num3:
        print ("El numero mayor es: ",num1)
elif num2>num1:
    if num2>num3:
        print ("El numero mayor es: ",num2)
elif num3>num1:
    if num3>num2:
        print ("El numero mayor es: ",num3)