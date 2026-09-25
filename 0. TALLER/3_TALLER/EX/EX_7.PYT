limite = int(input("Indique el numero limite a validar: "))
sumatoria=0
for i in range (limite+1):
    if i % 2!=0:
        print(i)
        print('-'*50)
        sumatoria = sumatoria+i
        print(sumatoria)

print(f"La sumatoria es: {sumatoria}")
    