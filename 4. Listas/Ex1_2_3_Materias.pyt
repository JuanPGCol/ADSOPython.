lim_Materias=int(input("Indique la cantidad de materias: "))
print('-'*50)

lis_Materia=[]
lis_Nota=[]

for i in range (lim_Materias):

    materia=str(input("Indique la materia a evaluar: "))
    lis_Materia.append(materia)
    nota=float(input("Indique la nota de la materia: "))
    lis_Nota.append(nota)
    print('-'*50)


#Validacion de notas

print(f"las notas son las siguientes: {lis_Nota }" )
for i in range (lim_Materias):
    print(f"La materia {lis_Materia[i]}: {lis_Nota[i] }" )
    if lis_Nota[i] >=3:
            print ("Aprobo la materia")
    else:
            print("No aprobo la materia")
    i=i+1
print('-'*50)
print(lis_Materia,lis_Nota)