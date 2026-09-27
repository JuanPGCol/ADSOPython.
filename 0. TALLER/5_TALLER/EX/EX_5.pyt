frase = str(input("Indique la frase a validar: ").lower())
fraseLetras = list(frase)
dic_Letras = {}

print (fraseLetras)

for comparacion in fraseLetras:
    if comparacion in dic_Letras:
        dic_Letras[comparacion] += 1
    else:
        dic_Letras[comparacion] = 1

for letra, contador in dic_Letras.items():
    print(f"{letra} : {contador}")