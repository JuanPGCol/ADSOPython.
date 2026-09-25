lis_Materia=["Matematicas","Ingles","Español","Ciencias"]
lis_NotPasada=[]
lis_MatPasada=[]

for i in range (4):
    nota = float(input(f"Indique la nota de {lis_Materia[i]}:"))
    if nota>=3.0:
        lis_MatPasada.append(lis_Materia[i])
        lis_NotPasada.append(nota)

for i in range(4):
    print (f"las materias pasadas son: {lis_NotPasada[i]}{lis_MatPasada[i]}")