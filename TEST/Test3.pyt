def menu():
    print (preguntas[1])
    print ("2.b")
    print ("3.c")
    print ("4.d")
    print ("5.e")

comodin1 = 1
comodin2 = 1
comodin3 = 1

def descarte():
    #Se encarga de quitar 2 de las 3 preguntas erroneas
    if comodin1 == 1:
        print ("Fueron descartadas ")
        comodin1 - 1
    else:
        print("No tiene comodin disponible")

def llamada():
    #Da directamente la respuesta
    if comodin2 == 1:
        print (f"La respuesta es:")
        comodin2 - 1
    else:
        print("No tiene comodin disponible")

def cambio():
    #Realiza el cambio de la pregunta por una del segundo listado
    comodin3 - 1
    if comodin3 == 1:
        print (f"Se realizara el cambio de pregunta")
        comodin3 - 1
    else:
        print("No tiene comodin disponible")


preguntas = {1:"¿Cuál es el río más largo del mundo?"
             ,2:"¿En qué año cayó el Muro de Berlín?"
             ,3:"¿Quién pintó la obra La noche estrellada?"
             ,4:"¿Cuál es el país más grande del mundo por extensión territorial?"
             ,5:"¿Qué antigua civilización construyó la ciudadela de Machu Picchu?"}

pregCambio = {1:"¿Cuál es el elemento químico más abundante en el universo?"
             ,2:"¿Cuál es el animal terrestre más veloz del planeta?"
             ,3:"¿En qué año llegó el ser humano a la Luna por primera vez?"
             ,4:"¿Qué órgano del cuerpo humano produce la hormona insulina?"
             ,5:"¿Qué gas compone la mayor parte de la atmósfera terrestre?"}

menu()
