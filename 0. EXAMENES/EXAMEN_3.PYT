ingresos=0
puntaje=0
antiguedad=0

while ingresos==0 and puntaje==0 and antiguedad==0:
    ingresos=float(input(f"Indique el valor de los ingresos mensuales: "))
    puntaje=float(input(f"Ingrese el puntaje crediticio: "))
    antiguedad=float(input(f"Ingrese los años de antiguedad laboral: "))
    if ingresos==0 and puntaje==0 and antiguedad==0:
        print(f"-"*50)
        print("Por favor indique los valores a validar")
        print(f"-"*50)

if ingresos >=4000000 and puntaje>=750 and antiguedad>=2:
    print(f"-"*50)
    print (f"Su solicitud se encuentra en estado: Aprobado")
    print(f"-"*50)
elif ingresos >=4000000 and puntaje>=750:
    print(f"-"*50) 
    print(f"Su solicitud se encuentra en estado: En estudio")
    print(f"-"*50)
elif ingresos >=4000000 and antiguedad>=2:
    print(f"-"*50)
    print(f"Su solicitud se encuentra en estado: En estudio")
    print(f"-"*50)
elif puntaje >=750 and antiguedad>=2:
    print(f"-"*50)
    print(f"Su solicitud se encuentra en estado: En estudio")
    print(f"-"*50)
else: 
    print(f"-"*50)
    print (f"Su solicitud fue Rechazada")
    print(f"-"*50)