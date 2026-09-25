limite = int(input("Indique la cantidad de estudiantes a ingresar: "))
print('-'*50)
dic_Estudiantes = {}

for i in range (limite):
    dic_Estudiantes.update({int(input("Codigo del estudiante: ")) : str(input("Nombre del estudiante: "))})
    if i < limite-1:
        print('------Siguiente estudiante------')
    else:
        print("---------------//---------------")

print ("El listado de estudiantes es: ")
for codigo, estudiante in dic_Estudiantes.items():
    print (f" {codigo} -> {estudiante}")
print('-'*50)