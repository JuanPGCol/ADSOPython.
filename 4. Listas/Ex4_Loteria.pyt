lim_Numeros=int(input("Indique la cantidad de numeros ganadores: "))
lis_Ganadores=[]

for i in range (lim_Numeros):

    loteria=int(input("Indique el numero ganador: "))
    lis_Ganadores.append(loteria)
print('-'*50)

#Informacion de salida
lis_Ganadores.sort()

for i in range (lim_Numeros):
    print("Los numeros ganadores son:" ,lis_Ganadores[i])