#El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación:
#1->15000, 2->24000, 3->36000
#Si cada ingrediente adicional cuesta $4.000. Escribir un programa que solicite al empleado encargado de registrar las ventas, el tamaño de la pizza y el número de ingredientes adicionales y muestre al cliente el precio que debe pagar.

tamaño = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))

if tamaño == 1:
    precio = 15000
elif tamaño == 2:
    precio = 24000
elif tamaño == 3:
    precio = 36000
else:
    print("Tamaño de pizza inválido. Por favor, ingrese 1, 2 o 3.")
    exit()

adicional = int(input("Ingrese el número de ingredientes adicionales: "))

precio_ingredientes = adicional * 4000

total = precio + precio_ingredientes

print("El precio total a pagar es: $", precio, "+ $", precio_ingredientes)
print("El precio total a pagar es: $", total)