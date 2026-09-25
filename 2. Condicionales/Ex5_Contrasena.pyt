passQ = str(input("Indique la contraseña: "))
passT = "admin123"
if  passQ == passT:
    print('-'*50)
    print ("Acceso concedido")
    print('-'*50)
else:
    print('-'*50)
    print ("Acceso denegado")
    print('-'*50)