limite = int(input("Indique la cantidad de numeros a ingresar: "))
lis_Digitos = []
lis_Ordenados = []
print('-'*50)

for i in range(limite):
    digito = int(input(f"indique el digito a almacenar: "))
    lis_Digitos.append(digito)

#Organizacion del listado W.Sort
for i in range(len(lis_Digitos)):
    menor = min(lis_Digitos)
    lis_Ordenados.append(menor)
    lis_Digitos.remove(min(lis_Digitos))
print('-'*50)
print('-'*50)

for i in range (len(lis_Ordenados)):
    print(lis_Ordenados[i])
print('-'*50)