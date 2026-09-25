#Datos
palabra = str(input("Indique la palabra a validar: "))
palInvertida=palabra

#Invertir 


#Validacion y printeo
if palabra == palInvertida[::-1]:
    print ("Es un palindromo")

else:
    print("No es palindromo")

#Validacion
#dividido=list(palabra)
#longitud=len(dividido)

#print(dividido[1])
#print(longitud)

#print(longitud%2==0)
#for i in range (longitud%2==0):
#    if dividido==dividido[-1]:
#        print ("Es palindromo")
#    else:
#        print ("No es palindromo")
