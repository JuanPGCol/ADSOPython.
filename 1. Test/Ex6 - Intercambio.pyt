#Datos a intercambiar
num1 = int(input("Indique el primer digito: "))
num2 = int(input("Indique el segundo digito: "))

#Intercambio
aux = num1
num1 = num2
num2 = aux

#Salida
print("--------------------------------------------")
print("El primer digito ahora es ",num1," y el segundo digito ahora es ",num2)
print("--------------------------------------------")