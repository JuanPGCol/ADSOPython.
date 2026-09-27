dic_Empleados = {101:2500000,102:3200000,103:2800000}

nomina = sum(dic_Empleados.values())
promedioNomina = nomina/len(dic_Empleados)
print(f"El salario promedio es: {promedioNomina}")