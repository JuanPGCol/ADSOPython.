usuario=str(input("Indique el usuario: "))
contasenia=str(input("Indique la contraseña: "))

#usAcceso = "Admin"
#coAcceso = "Admin123"

#Roles
roles={"Admin":"Admin123","Supervisor":"Super123","Caja":"Caja123"}

#Validacion de acceso
if usuario == roles.keys:
    print ("Acceso concedido")

else:
    print ("Acceso bloqueado")

#Opciones a tomar
lis_Opciones=["1. Modificar contraseña","2. Revisar informes","3.Gestionar permisos"]

