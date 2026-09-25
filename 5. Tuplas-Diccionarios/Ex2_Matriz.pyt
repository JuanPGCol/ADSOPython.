matriz1=[(1,2,3),
         (4,5,6)]
matriz2=[(-1,0),
         (0,1),
         (1,1)]

#Calculo
for paquete in range (len(matriz1)):
    for spaquete in range (len(matriz2)):
        for sspaquete in range (len(matriz2)):
            print (f"Paquete {paquete} | contenido = {matriz1[paquete][spaquete]}")