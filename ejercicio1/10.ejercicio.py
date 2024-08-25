
diario = int(input("Ingrese el salario diario del empleado: "))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))

salario = diario * dias_trabajados
pension = salario * 0.10
salud = salario * 0.15
completo = salario - pension - salud

print(f"Salario bruto: {salario}")
print(f"Descuento por pensión (10%): {pension}")
print(f"Descuento por salud (15%): {salud} ")
print(f"Salario neto a pagar: {completo}")
