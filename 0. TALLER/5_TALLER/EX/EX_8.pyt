dic_Libros = {"L001":"Python Básico","L002":"Estructuras de Datos","L003":"Bases de Datos"}

consulta = str(input("indique el codigo del libro a consultar: ").upper())

if consulta in dic_Libros:
    print (f"Se encontro el libro requerido: \n{consulta} -> {dic_Libros[consulta]} ")

else:
    print("El libro no fue encontrado")