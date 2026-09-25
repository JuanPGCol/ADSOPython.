palabra = str(input("Indique una palabara para contar las vocales: "))
vocales = 0

for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vocales += 1

print (f"La cantidad de vocales en la palabra indicada es: {vocales}")