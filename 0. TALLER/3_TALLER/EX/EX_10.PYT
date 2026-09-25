terminos = int(input("Indique la cantidad de terminos a calcular: "))
n2=0

for n1 in range (terminos):
    n2+=1
    calculo = n1 + n2
    print(f"El calculo del termino {n2}. {n1} y {n2} es : {calculo}")
