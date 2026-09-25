limite = int(input("Indique la cantidad de productos a ingresar: "))
print('-'*50)
lis_Compras = []

for i in range (limite):
    producto = str(input("Indique el producto a comprar: "))
    lis_Compras.append(producto)
print('-'*50)  

print("La lista de compras es: ")
for i in range (len(lis_Compras)):
    print (f"{i+1}.{lis_Compras[i]}")
print('-'*50)