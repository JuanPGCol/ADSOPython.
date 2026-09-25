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

lis_Correcta = ["a","b","c","d","a"]
lis_Correcta2 = ["b","a","b","d","a"]

for id, pregunta in preguntas.items():
    print(id, pregunta)
    resp = str(input("Responda la pregunta: "))
    if resp in lis_Correcta:
        print ("Correcto...")
    else:
        print ("Fin del juego...")
        break