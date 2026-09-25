tamanio = int(input("Indique la cantidad de digitos a ingresar: "))
list_Digitos=[]

for i in range (tamanio):
    digitos = int(input("Indique el digito a validar: "))
    list_Digitos.append(digitos)

#Organizar listado
list_Digitos.sort()

#Mostrar digito más alto
print(f"El segundo digito más grande de los indicados es: {list_Digitos[tamanio-2]}")
print("-"*25)
print(f"Listado de numeros: {list_Digitos}")
print("-"*25)