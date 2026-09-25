palabra=str(input("Indique una palabra para contar las vocales: ")).lower()


if palabra.count("a")>0:
    print (f"La cantidad de vocales A es:{palabra.count("a")}")
if palabra.count("e")>0:
    print (f"La cantidad de vocales E es:{palabra.count("e")}")
if palabra.count("i")>0:
    print (f"La cantidad de vocales I es:{palabra.count("i")}")
if palabra.count("o")>0:
    print (f"La cantidad de vocales O es:{palabra.count("o")}")
if palabra.count("u")>0:
    print (f"La cantidad de vocales U es:{palabra.count("u")}")