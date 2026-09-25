limite = int(input(f"Indique la cantiad de numeros a ingresar: "))
lis_Digitos=[]

for i in range (limite):
    digito=int(input(f"Indique el digito a almacenar: "))
    lis_Digitos.append(digito)

#Consulta
print('-'*50)
busqueda = int(input(f"Indique un numero a buscar: "))
print('-'*50)

conteo = lis_Digitos.count(busqueda)

for i in range (limite):

    if busqueda == lis_Digitos[i]:
        print(f"El numero {busqueda} se encuentra en la lista y esta en la posicion {i+1}")

        if conteo >= 2:
            print (f"La cantidad de veces que se repite el digito es: {conteo}")
        print('-'*50)
        break

    elif i == limite-1:
        print(f"El numero no esta en la lista")