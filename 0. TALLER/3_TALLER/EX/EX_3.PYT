tabla = int(input("Indique una tabla a validar: "))

inicio = 1

for i in range(10):
    i+=1
    calculo=i*tabla
    print(f"{i} X {tabla} = {calculo}")