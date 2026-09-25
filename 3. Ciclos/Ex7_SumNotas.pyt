

inicio = 1
limite = 5
nota1 = 0

while inicio <= limite:
    nota0 = float(input("Indique la siguiente nota: "))
    nota1 = nota1 + nota0
    inicio = inicio + 1
nota1 = nota1/limite
print ("La sumatoria de notas es: ",nota1)