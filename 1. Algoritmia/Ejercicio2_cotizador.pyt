#Datos de factura
nombreCliente = str(input("Ingrese el nombre del cliente"))
persona = str(input("ingrese el tipo de persona (Natural o juridica)"))

#Componentes
cpu=str(input("Ingrese la marca o referencia del procesador"))
cpuValor=float(input("Ingrese el valor del procesador"))
ram=str(input("ingrese la marca o referencia de la memoria ram"))
ramValor=float(input("ingrese el valor de la memoria ram"))
storage=str(input("ingrese la marca o referencia de la unidad de almacenamiento"))
storageValor=str(input("ingrese el valor de la unidad de almacenamiento"))

#Cotizador
print("-------Cotizacion-------")
print("-------Datos del cliente-------")
print("Cliente: ",nombreCliente)
print("Tipo de cotizacion: ",persona)
print("--------------")
print("--------------")