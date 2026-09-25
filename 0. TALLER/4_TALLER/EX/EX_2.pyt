cantCalificaciones= int(input("Indique la cantidad de notas a registrar: "))
lis_notas=[]

for i in range (cantCalificaciones):
    nota=float(input("Indique la nota a calcular: "))
    lis_notas.append(nota)

sumatoria = 0
for i in range (cantCalificaciones):
    sumatoria = sumatoria + lis_notas[i]
    print(sumatoria)

print('-'*50)
promedio = sumatoria/cantCalificaciones
print(f"Las notas almacenadas son: {lis_notas}")
print(f"El promedio de las notas es: {promedio}")