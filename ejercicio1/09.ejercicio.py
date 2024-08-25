# Programa que permita a una tienda saber el valor que pagara un cliente por la compr
# a de varios elementos de la misma referencia. 
# Debe tener como entradas el valor unitario, 
# la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

precio = int(input("Ingrese el precio del producto: "))
n = int(input("Ingrese la cantidad de productos que comprara: "))
iva = 1.16
total = precio * n * iva

print("El valor total a pagar es: ", total)
