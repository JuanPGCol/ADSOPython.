nota = float(input("Indique la nota del estudiante: "))
asistencia = int(input("Indique la asistencia del estudiante: "))

#Decision
if nota >= 3.0 and asistencia >= 80:
    print('-'*50)
    print("El estudiante aprobo la materia")
    print('-'*50)
else:
    print('-'*50)
    print("El estudiante no aprobo la materia")
    print('-'*50)