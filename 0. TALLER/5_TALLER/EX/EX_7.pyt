dic_Vendedores = {"Laura":4500000,"Juan":6200000,"Pedro":5100000}

print (f"Listado de vendedores en el sistema: {dic_Vendedores}")
print ('='*30)
newVendor = str(input("Indique el nombre del nuevo vendedor: "))
newSell = float(input("Indique el valor de las ventas realizadas: "))
dic_Vendedores.update({newVendor:newSell})
print(dic_Vendedores)
print ('='*30)
mejorV = max(dic_Vendedores,key=dic_Vendedores.get)

print(f"El mejor vendeor es: {mejorV} -> ${dic_Vendedores[mejorV]}")