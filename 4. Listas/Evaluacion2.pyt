limite = int(input("Indique el numero hasta el cual se generaran los numeros pares: "))


lis_Pares=[]

#Calculo

for i in range (limite):
    
    if i%2==0:
        lis_Pares.append(i)
print(lis_Pares)