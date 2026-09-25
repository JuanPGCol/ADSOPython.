def sumar (numero1, numero2):
    return (numero1 + numero2)
def restar (numero1, numero2):
    return (numero1 - numero2)
def multiplicar (numero1, numero2):
    return (numero1 * numero2)
def dividir (numero1, numero2):
    return (numero1 / numero2)
    
while True:
    print("Menu de operaciones")
    print("----------//----------")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")

    operacion = int(input("Indique la operacion a realizar: "))
    numero1 = float(input("Indique el primer digito: "))
    numero2 = float(input("Indique el segundo digito: "))
    print ("-"*30)  

    if operacion == 1:
        print ("Se realizara la suma de los numeros indicados")
        resultado = sumar (numero1, numero2)
        
    elif operacion == 2:
        print ("Se realizara la resta de los numeros indicados")
        resultado = restar (numero1, numero2)
        
    elif operacion == 3:
        print ("Se realizara la multiplicacion de los numeros indicados")
        resultado = multiplicar (numero1, numero2)
        
    elif operacion == 4:
        print ("Se realizara la division de los numeros indicados")
        resultado = dividir (numero1, numero2)
        
    elif operacion == 5:
        print ("Se selecciono la opcion cancelar \n Cerrando programa")
    
    print ("-"*30)    
    print (f"El resultado de la operacion {operacion} es: {resultado}")
    print ("-"*30)  
    break