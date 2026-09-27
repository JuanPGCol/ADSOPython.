frase = str(input("Indique la frase a validar: ").lower())
fraseSeparada = frase.split()
dic_Frase = {}

for comparacion in fraseSeparada:
    if comparacion in dic_Frase:
        dic_Frase[comparacion] += 1
    else:
        dic_Frase[comparacion] = 1

for palabra, contador in dic_Frase.items():
    print(f"{palabra} : {contador}")