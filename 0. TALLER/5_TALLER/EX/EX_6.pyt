dic_Estudiantes = {}
cantEstudiantes = int(input("Indique la cantidad de estudiantes a ingresar: "))

for i in range(cantEstudiantes):
    dic_Estudiantes.update({input("Indique el nombre del estudiante: "):float(input("Indique la nota del estudiante: "))})

for estudiante, nota in dic_Estudiantes.items():
    print(f"{estudiante} : {nota}")



mejorE = max(dic_Estudiantes,key=dic_Estudiantes.get)

print(f"El estudiante con la mejor nota es: {mejorE} -> {dic_Estudiantes[mejorE]}")