limite = int(input("Indique la cantidad de numeros a ingresar: "))
lis_Digitos =[]
print(f"-"*50)


for i in range (limite):
    digito = float(input("Indique el digito a ingresar en el listado: "))
    lis_Digitos.append(digito)
print(f"-"*50)
for i in range (limite):
    
    print(f"Los digitos ingresados en el listado son: {lis_Digitos[i]}") 

minimo = min(lis_Digitos)
maximo = max(lis_Digitos)

print(f"-"*50)
print(f"El digito mayor es: {maximo}")
print(f"El digito menor es: {minimo}")
print(f"-"*50)