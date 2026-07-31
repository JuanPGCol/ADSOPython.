#Datos iniciales
distancia = float(input("Indique la cantidad de kilometros recorridos: "))
consumo = float(input("Indique la cantidad de combustible usado: "))

#Calculos
galonesUsados = consumo/distancia

#Informacion final
print("Basado en los datos indicados, el consumo por kilometro fue de: ",galonesUsados, " galones")