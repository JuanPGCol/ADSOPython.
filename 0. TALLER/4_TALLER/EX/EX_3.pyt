limite = int(input(f"Indique la cantidad de numeros a ingresar: "))
lis_Digitos =[]
lis_DigitosP = []
lis_DigitosN =[]

for i in range (limite):
    digito = int(input(f"Indique el digito a almacenar: "))
    lis_Digitos.append(digito)
    if digito % 2==0:
        lis_DigitosP.append(digito)
    else:
        lis_DigitosN.append(digito)

conteoP=lis_DigitosP.__len__()
conteoN=lis_DigitosN.__len__()

print('-'*50)
print(f"La cantidad de digitos positivos es: {conteoP}")
print (lis_DigitosP)
print('-'*50)
print(f"La cantidad de digitos negativos es: {conteoN}")
print(lis_DigitosN)
print('-'*50)
