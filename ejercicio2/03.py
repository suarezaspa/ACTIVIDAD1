#Solicitar número al usuario y determinar si es negativo, positivo o cero.

numero = int(input("Ingrese un número: "))
if numero < 0:
    print("El número es negativo")
elif numero > 0:
    print("El número es positivo")
else:
    print("El número es cero")