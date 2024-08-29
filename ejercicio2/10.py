#Leer el número de llantas de una compra y mostrar el valor que debe pagarse. El almacén las vende con la siguiente política: Si se compran menos de 6 llantas, el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000, y si se compran más de 7 llantas, el precio unitario es $180000.

def calcular_valor_a_pagar(llantas):
    if llantas < 0:
        return "Error: El número de llantas no puede ser negativo."
    elif llantas < 6:
        return f"El valor a pagar es: {llantas * 240000}"
    elif 6 <= llantas <= 7:
        return f"El valor a pagar es: {llantas * 221000}"
    else:
        return f"El valor a pagar es: {llantas * 180000}"

try:
    llantas = int(input("Ingrese el número de llantas que quiere comprar: "))
    print(calcular_valor_a_pagar(llantas))
except ValueError:
    print("Error: Por favor ingrese un número entero.")
