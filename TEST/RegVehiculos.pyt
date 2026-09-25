lis_placa = ["DQQ34H","ZZZ011","ZTR06A"]
lis_Marca = ["SUZUKI","MUSTANG","YAMAHA"]
lis_AnioFab = [2023,1980,2025]


def consulta():
    #Realiza la busqueda en un listado
    busqueda = str(input("Indique la placa a buscar: "))

while True:

    print (f"============== MENÚ ==============")
    print ("1. Registrar vehículo \n2. Mostrar vehículos \n3. Buscar vehículo \n4. Mostrar vehículo más antiguo\n5. Mostrar año promedio de fabricación \n6. Salir")
    print ("==================================")

    seleccion = int(input("Seleccione una opcion del menú: "))

    if seleccion > 0 and seleccion <= 6:

        promedioFab = 0
        for i in lis_AnioFab:
            promedioFab += i
        promedioFab = promedioFab/len(lis_AnioFab)

        if seleccion == 1:
            placa = (str(input("Indique la placa del vehiculo: "))).upper()
            lis_placa.append(placa)
            marca = (str(input("Indique la marca del vehiculo: "))).upper()
            lis_Marca.append(marca)
            anio = (int(input("Indique el año de fabricacion del vehiculo: ")))
            lis_AnioFab.append(anio)

            antiguo = min(lis_AnioFab)
            reciente = max(lis_AnioFab)
            print (antiguo , reciente)
            
            print ("Vehiculo ingresado...")
            print (print('='*35))

        elif seleccion == 2:
            for i in range (len(lis_placa)):
                print (f"Los vehiculos son los siguientes:")
                print (f"{lis_placa[i]} - {lis_Marca[i]} - {lis_AnioFab[i]}")
            if len(lis_placa) == 0:
               print ("No hay vehiculos registrados")

        elif seleccion == 3:
            buscador = str(input("Indique la placa a buscar: ")).upper()

            if buscador in lis_placa:
                search = lis_placa.index(buscador)
                print (f"El vehiculo {lis_placa[search]} es {lis_Marca[search]} y fue fabricado en el año {lis_AnioFab[search]}")

            else:   
                print ("El vehiculo no fue encontrado")

        elif seleccion == 4:
            print (f"El vehiculo más antiguo es del año {antiguo}")
            print (f'='*35)

        elif seleccion == 5:
            print (f"El promedio de de fabricacion es {promedioFab}")
            print (f'='*35)

        elif seleccion == 6:
            print ("Ha seleccionado salir del sistema...")
            break