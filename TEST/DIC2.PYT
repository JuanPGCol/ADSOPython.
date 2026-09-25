dic_TD = {
    "482915": {"Nombre" : "Juan Pérez","TD" : "CC"},
    "730184": {"Nombre" : "María García","TD" : "TI"},
    }
while True:

    
    print("Menu de operaciones")
    print("----------//----------")
    print("1. ingresar nuevos datos\n2. Consultar BD\n3. Consultar un dato\n4. Cerrar")
    print("----------//----------") 

    seleccion = int(input("Seleccione la opcion requerida: "))

    match seleccion:

        case 1:
        
            dic_TD.update({int (input("indique el documento a ingresar: ")): str (input("indique el nombre a ingresar: "))})
                
        case 2:
            for i in dic_TD:
                 print (f"{dic_TD} y el documento es {dic_TD}")
        
        case 3:
            buscador = str(input("Indique el numero de documento a consultar: "))

            if buscador in dic_TD:

                 
                print (f"el documento consultado se encontró:\n {buscador} - {dic_TD[buscador][i]}  -  {dic_TD[buscador]["TD"]}")

            else:
                print("El ID no fue encontrado")

        case 4:
            print ("Usted selecciono salir del programa...")
            break