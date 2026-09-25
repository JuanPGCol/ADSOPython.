canNotas = int(input("Indique la cantidad de notas: "))

sumatoria=0

for i in range (canNotas):
    nota = float(input("Indique la nota a evaluar: "))
    sumatoria = sumatoria+nota
    promedio = sumatoria/canNotas

print(f"La nota promedio del estudiante es: {promedio}")