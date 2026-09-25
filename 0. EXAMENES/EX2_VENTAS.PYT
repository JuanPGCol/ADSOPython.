lis_ventas = []

limite = int(input("Indique la cantidad de días a validar: "))

#Almacenamiento de ventas

for i in range (limite):
    valor = float(input(f"Indique el valor de la venta del día {i+1}: "))
    lis_ventas.append(valor)

ventaMin = min(lis_ventas)
ventaMax = max(lis_ventas)

#Promedio y total de ventas

promedioVenta = 0
ventasEncProm = 0

for i in lis_ventas:
    sumaVentas = (promedioVenta + i)

PromVentas = sumaVentas/7

for i in lis_ventas:
    if i > PromVentas:
        ventasEncProm = ventasEncProm + 1

#Informacion requerida

print (f"La venta más alta fue: {ventaMax}")
print (f"La venta más baja fue: {ventaMin}")
print (f"El total de ventas fue: {sumaVentas}")
print (f"El promedio de ventas es: {PromVentas}")
print (f"Ventas por encima del promedio: {ventasEncProm}")