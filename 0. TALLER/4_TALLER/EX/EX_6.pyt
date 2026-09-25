limite = int(input("Indique la cantidad de palabras a ingresar: "))
lis_Digitos=[]

for i in range(limite):
    digito = int(input(f"indique el digito a almacenar: "))
    lis_Digitos.append(digito)

#Lista sin duplicados
lis_WDuplicados = list(set(lis_Digitos))

print('-'*50)
print(f"El listado sin duplicados es:")
print('-'*50)

for i in range (len(lis_WDuplicados)):
    print(f"{lis_WDuplicados[i]}")
print('-'*50)