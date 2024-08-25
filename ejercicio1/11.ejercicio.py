
n = float(input("Ingrese un número para calcular su raíz cuadrada: "))

if n < 0:
    print("El número no puede ser negativo.")
else:

    aproximacion = n / 2
                                               #No encontré de otra. Debe haber una forma más sencilla de hacerlo :skull:
    for i in range(20):
        aproximacion = (aproximacion + n / aproximacion) / 2

    print(f"La raíz cuadrada aproximada de {n} es: {aproximacion}")
