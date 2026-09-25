numeros = int(input("Indique la cantidad de numeros a ingresar: "))

positvos=0
negativos=0
ceros=0

for i in range (numeros):
    digito=float(input("Indique el numero: "))
    if digito>0:
        positvos=positvos+1
    elif digito<0:
        negativos=negativos+1
    elif digito==0:
        ceros=ceros+1

    
print (f"-"*50)
print (f"Numeros positivos: {positvos}")
print (f"Numeros negativos: {negativos}")
print (f"Numeros en cero: {ceros}")