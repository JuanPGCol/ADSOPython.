frase = str(input("Indique la frase a validar: "))
div = frase.split()

dic_Frase = {}
contador = 0

#Comparacion de strings
for palabra in div:
    if palabra != div:
        dic_Frase.update({palabra : contador})

    if palabra == div:
        dic_Frase.update({contador += 1})

#Informacion necesaria
for palabra, contador in dic_Frase.items():
    print (palabra, contador)

