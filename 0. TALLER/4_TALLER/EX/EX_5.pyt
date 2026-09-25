limite = int(input("Indique la cantidad de palabras a ingresar: "))

lis_palabras=[]

for i in range (limite):

    palabra = str(input(f"Indique la palabra a almacenar: "))
    lis_palabras.append(palabra)

lis_palabras.reverse()
for i in range(limite):
    print (lis_palabras[i])