lis_Tiempos = []

atletas = int(input("Indique la cantidad de atletas que competiran: "))

#Almacenamiento de tiempos

for i in range (atletas):
    tiempo = float(input(f"Indique los tiempos del corredor {i+1}: "))
    lis_Tiempos.append(tiempo)

tiempoMin = min(lis_Tiempos)
tiempoMax = max(lis_Tiempos)

#Promedio de tiempos

promedioTiempo = 0

for i in lis_Tiempos:
    promedioTiempo = (promedioTiempo + i)

PromTiempos = promedioTiempo/atletas

bajoPromTiempo = 0

for i in lis_Tiempos:
    if i < PromTiempos:
        bajoPromTiempo = bajoPromTiempo + 1

#Informacion requerida

print (f"El mayor timepo es: {tiempoMax}s")
print (f"El menor timepo es: {tiempoMin}s")
print (f"El tiemopo promedio es: {PromTiempos}s")
print (f"Atletas por debajo del promedio: {bajoPromTiempo}")