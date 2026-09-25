lis_nombre = ["Juan","María","Carlos","Ana","Luis","Laura","José","Carmen","Pedro","Isabel","Miguel","Elena","Jorge","Marta","Andrés","Lucía","Fernando","Paula","David","Sofía","Alejandro","Valeria","Diego","Camila","Javier","Valentina","Roberto","Gabriela","Ricardo","Daniela"]
lis_apellidos = ["Pérez","García","López","Rodríguez","Martínez","Hernández","González","Gómez","Fernández","Díaz","Álvarez","Ruiz","Alonso","Jiménez","Moreno","Muñoz","Romero","Navarro","Torres","Domínguez","Vargas","Ramos","Castro","Ortiz","Silva","Morales","Herrera","Medina","Flores","Ríos"]
lis_doc = [482915,730184,105923,629471,854209,913847,3502841,8194027,2475819,6038152,9714283,4281905,59281743,14092837,83719402,36281904,70592814,91827364,482019385,739104826,150294837,829471035,604819273,391827405,2849103857,6928174035,1049283715,8573910284,4719283056,9302847192]

while True:

    
    print("Menu de operaciones")
    print("----------//----------")
    print("1. ingresar nuevos datos\n2. Consultar BD\n3. Consultar un dato\n4. Cerrar")
    print("----------//----------") 

    seleccion = int(input("Seleccione la opcion requerida: "))

    match seleccion:

        case 1:
            documento = int (input("indique el documento a ingresar: "))
            lis_doc.append(documento)
            nombre = str (input("indique el nombre a ingresar: "))
            lis_nombre.append(nombre)
            apellido = str (input("indique el apellido a ingresar: "))
            lis_apellidos.append(apellido)
                
        case 2:
            for i in range (len(lis_doc)):
                 print (f"El nombre del caso {i} es {lis_nombre[i]} {lis_apellidos[i]} y el documento es {lis_doc[i]}")
        
        case 3:
            buscador = int(input("Indique el numero de documento a consultar: "))

            if buscador in lis_doc:

                search = lis_doc.index(buscador)
                print (f"el documento consultado se encontró:\nCC {lis_doc[search]} - {lis_nombre[search]} {lis_apellidos[search]}")

            else:
                print("El ID no fue encontrado")

        case 4:
            print ("Usted selecciono salir del programa...")
            break