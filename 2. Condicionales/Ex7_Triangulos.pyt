lado1 = float(input("Indique la longitud del primer lado: "))
lado2 = float(input("Indique la longitud del segundo lado: "))
lado3 = float(input("Indique la longitud del tercer lado: "))

#Validacion | Tipo de triangulo
if lado1 == lado2 and lado2 == lado3:
    print ("El triangulo es Equilatero")
elif lado1 != lado2 and lado2 == lado3:
    print ("El triangulo es escaleno")
elif lado1 != lado2 and lado2 != lado3:
    print("El triangulo es Isoceles")