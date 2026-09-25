palabra = str(input("Indique una palabra a validar: ")).lower()
desPalabra=list(palabra)

vocal = 0

for i in palabra:
    if i in "aeiou":
        vocal=vocal+1
    
print (f"La cantidad de vocales es: {vocal}")
print(desPalabra)