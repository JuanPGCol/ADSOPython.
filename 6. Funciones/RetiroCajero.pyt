saldo = 1750905
def retcon (valor, saldo):
    return (saldo - valor)
def depositar (valor, saldo):
    return (saldo + valor)

while True:
    contrasenia = (str(input("Indique la contraseña: ")))
    if contrasenia == "admin123":
        print("Menu de operaciones")
        print("----------//----------")
        print("1. Retirar efectivo\n2. Consultar saldo\n3. Depositar efectivo\n4. Transferir dinero\n5. Cancelar operacion")
        print("----------//----------") 
        operacion = str(input("Indique la operacion a realizar: "))

        match operacion:
            case "1":
                valor = (int(input("Indique el valor a retirar: ")))
                nuevoSaldo = retcon (saldo, valor)
                print("----------//----------")
                print (f"Saldo: {nuevoSaldo}")
                print("----------//----------")
                cont = (str(input("Desea realizar otra operacion: ")))
                if cont == "no":
                    break
            case "2":
                print (saldo)
                cont = (str(input("Desea realizar otra operacion: ")))
                if cont == "no":
                    break
            case "3":
                valor = (int(input("Indique la cantidad de depositar: ")))
                nuevoSaldo = depositar (saldo, valor)
                print("----------//----------")
                print (nuevoSaldo)
                print("----------//----------")
                cont = (str(input("Desea realizar otra operacion: ")))
                if cont == "no":
                    break
            case "4":
                valor = (int(input("indique el valor a transferir: ")))
                nuevoSaldo = retcon (saldo, valor)
                print("----------//----------")
                print (nuevoSaldo)
                print("----------//----------")
                cont = (str(input("Desea realizar otra operacion: ")))
                if cont == "no":
                    break
            case "5":
                print ("Operacion cancelada")
                break
            case _:
                print ("Seleccione de las opciones mostradas")
    else:
        print("Contraseña incorrecta, el sistema se bloqueara")
        print("BLOQUEADO")
        break