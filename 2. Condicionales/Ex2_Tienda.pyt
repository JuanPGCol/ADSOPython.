valorCompra = float(input("Indique el valor de la compra: "))

#Calculo para tomar decision | 20% de descuento

if valorCompra > 100000:
    valorDesc = (valorCompra*.2)
    valorPago = valorCompra-valorDesc
    print('-'*50)
    print ("Se aplicara descuento a la compra")
    print('-'*50)
    print ("El descuento es de ",valorDesc," y el valor del pago total es ",valorPago)
    print('-'*50)
else:
    print('-'*50)
    print("Al valor no aplica descuento")
    print('-'*50)
    print("El valor a pagar es ",valorCompra)
    print('-'*50)