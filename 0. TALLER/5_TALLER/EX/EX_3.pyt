limite = int(input("Indique la cantidad de contactos a agregar: "))
print('-'*50)
dic_Contactos = {}

for i in range (limite):
    dic_Contactos.update({str(input("Nombre del contacto: ".lower())) : int(input("Numero telefonico: ".lower()))})
    if i < limite-1:
        print('------Siguiente contacto------')
    else:
        print("---------------//---------------")

print ("El directorio telefonico es: ")
for contacto, numero in dic_Contactos.items():
    print (f" Nombre: {contacto}")
    print (f" Telefono: {numero}")

print('-'*50)

#Busqueda de contacto

busqueda = str (input("Indique el contacto a buscar: "))

for contacto, numero in dic_Contactos.items():
    if busqueda == contacto:
        print (f"El numero de telefono de {busqueda} es {numero}")
        break
    
if busqueda != contacto:
    print("No se encontro el contacto")