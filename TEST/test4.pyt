listado = [1,7,5,4,2,6,3,9,8]

for num1 in range (len(listado)):
    for num2 in range (len(listado)-1):
        if listado[num2] > listado[num2+1]:
            aux = listado[num2]
            listado[num2] = listado[num2+1]
            listado[num2+1] = aux
print (listado)