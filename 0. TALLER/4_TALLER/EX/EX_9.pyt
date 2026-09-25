limite = int(input("Indique la cantidad de numeros a ingresar: "))
lis_Numeros = []
lis_NumerosO = []

for i in range (limite):
    digito = int(input("Indique el digito a almacenar: "))
    lis_Numeros.append(digito)
    lis_NumerosO.append(digito)

lis_NumerosO.sort()

print(f"El segundo digito más grande es: {lis_NumerosO[limite-2]}")

