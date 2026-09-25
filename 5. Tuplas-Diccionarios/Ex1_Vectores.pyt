vector1=(1,2,3)
vector2=(-1,0,2)

calculo=0

#calculo
for i in range (len(vector1)):
#+= es igaul a (calculo = calculo + resultado obtenido)
    calculo += vector1[i]*vector2[i]
    
print(vector1,vector2)
print(calculo)