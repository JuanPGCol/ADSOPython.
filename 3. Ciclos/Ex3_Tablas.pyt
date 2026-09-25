tabla = int(input("Indique la tabla a consultar"))
inicio = 1
limite = 10
resul = tabla*inicio

#Generacion de tabla
while inicio<=limite:
    resul = tabla*inicio
    print (tabla," X ",inicio," = ",resul)
    inicio = inicio + 1