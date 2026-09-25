# Ejercicio 1. Tarifa de estacionamiento

## Enunciado

Un parqueadero cobra la tarifa de acuerdo con el tiempo de permanencia de un vehículo.

Las reglas son las siguientes:

- Hasta 2 horas: $6.000 por hora.
- Más de 2 horas y hasta 5 horas: $5.500 por cada hora.
- Más de 5 horas: $5.000 por cada hora.

Adicionalmente:

- Si el cliente pertenece al programa de fidelización, recibe un 10% de descuento sobre el total.
- Si el valor final supera los $40.000, se aplica un descuento adicional del 5%.

Desarrolle un programa que solicite:

- Cantidad de horas.
- Si pertenece o no al programa de fidelización (S/N).

Calcule y muestre el valor total a pagar.

### Ejemplo de entrada

```text
Horas: 8
Cliente frecuente: S
```

### Salida esperada

```text
Valor a pagar: $34200
```

---

# Ejercicio 2. Liquidación de un empleado

## Enunciado

Una empresa desea calcular el salario mensual de sus empleados.

Solicite:

- Nombre del empleado.
- Horas trabajadas.
- Valor de la hora.

Considere las siguientes condiciones:

- Las primeras 40 horas se pagan al valor normal.
- Las horas adicionales se pagan con un recargo del 50%.
- Si el salario bruto supera los $3.000.000, se descuenta el 8% por retención.
- Si el salario bruto supera los $5.000.000, se descuenta el 12%.

Finalmente muestre:

- Salario bruto.
- Descuento aplicado.
- Salario neto.

### Ejemplo de entrada

```text
Nombre: Laura
Horas trabajadas: 50
Valor hora: 70000
```

### Salida esperada

```text
Empleado: Laura
Salario bruto: $3850000
Descuento: $308000
Salario neto: $3542000
```

---

# Ejercicio 3. Clasificación de un préstamo bancario

## Enunciado

Un banco evalúa las solicitudes de crédito teniendo en cuenta tres criterios:

- Ingresos mensuales.
- Puntaje crediticio (0 a 1000).
- Años de antigüedad laboral.

Las reglas son las siguientes:

- El crédito es **Aprobado** si:
  - ingresos ≥ $4.000.000,
  - puntaje ≥ 750,
  - antigüedad ≥ 2 años.

- El crédito queda **En estudio** si cumple exactamente dos de las tres condiciones.

- El crédito es **Rechazado** si cumple una o ninguna condición.

Solicite los datos del solicitante y determine el estado de la solicitud.

### Ejemplo de entrada

```text
Ingresos: 4200000
Puntaje: 710
Antigüedad: 5
```

### Salida esperada

```text
Estado de la solicitud: En estudio
```