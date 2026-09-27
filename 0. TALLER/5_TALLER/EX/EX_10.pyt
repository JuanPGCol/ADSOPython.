dic_Estudiantes = {
    101:{"Nombre":"Laura","Edad":20,"Carrera":"Ingenieria","Promedio":4.6},
    102:{"Nombre":"Juan","Edad":22,"Carrera":"Sistemas","Promedio":3.9},
    103:{"Nombre":"Camila","Edad":21,"Carrera":"Electronica","Promedio":4.9}                             }

mejorPromedio = max(dic_Estudiantes.values(), key=lambda mejEstudiante : mejEstudiante["Promedio"])

print ('='*30)
print (f"El mejor promedio fue: {mejorPromedio["Promedio"]} y fue de {mejorPromedio["Nombre"]} con {mejorPromedio["Edad"]} años de edad")
print ('='*30)