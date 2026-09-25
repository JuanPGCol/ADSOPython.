dic_Usuario = {
"482915":"Juan Pérez",
"730184":"María García",
"105923":"Carlos López",
"629471":"Ana Rodríguez",
"854209":"Luis Martínez",
"913847":"Laura Hernández",
"3502841":"José González",
"8194027":"Carmen Gómez",
"2475819":"Pedro Fernández",
"6038152":"Isabel Díaz",
"9714283":"Miguel Álvarez",
"4281905":"Elena Ruiz",
"59281743":"Jorge Alonso",
"14092837":"Marta Jiménez",
"83719402":"Andrés Moreno",
"36281904":"Lucía Muñoz",
"70592814":"Fernando Romero",
"91827364":"Paula Navarro",
"482019385":"David Torres",
"739104826":"Sofía Domínguez",
"150294837":"Alejandro Vargas",
"829471035":"Valeria Ramos",
"604819273":"Diego Castro",
"391827405":"Camila Ortiz",
"2849103857":"Javier Silva",
"6928174035":"Valentina Morales",
"1049283715":"Roberto Herrera",
"8573910284":"Gabriela Medina",
"4719283056":"Ricardo Flores",
"9302847192":"Daniela Ríos"}

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
        
            dic_Usuario.update({int (input("indique el documento a ingresar: ")): str (input("indique el nombre a ingresar: "))})
                
        case 2:
            for i in range (len(dic_Usuario)):
                 print (f"El nombre del caso {i} es {dic_Usuario[i]} y el documento es {dic_Usuario[i]}")
        
        case 3:
            buscador = str(input("Indique el numero de documento a consultar: "))

            if buscador in dic_Usuario:
            
                print (f"el documento consultado se encontró:\nCC - {buscador} - {dic_Usuario[buscador]}")

            else:
                print("El ID no fue encontrado")

        case 4:
            print ("Usted selecciono salir del programa...")
            break