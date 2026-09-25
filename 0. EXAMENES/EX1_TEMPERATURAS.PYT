lis_temp = []

for i in range (7):
    temp = float(input(f"Indique la temperatura del día {i+1}: "))
    lis_temp.append(temp)

tempMin = min(lis_temp)
tempMax = max(lis_temp)

promedioTemp = 0

for i in lis_temp:
    promTemp = (promedioTemp + i)

PromTemperatura = promTemp/7

diasProm = 0

for i in lis_temp:
    if i > PromTemperatura:
        diasProm = diasProm + 1

print (f"La temperatura maxima es: {tempMax}")
print (f"La temperatura minima es: {tempMin}")
print (f"La temperatura promedio es: {PromTemperatura}")
print (f"Días por encima del promedio: {diasProm}")