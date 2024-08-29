#Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    print("El número mayor es: ", num1)
    print("El número menor es: ", num2)
else:
    print("El número mayor es: ", num2)
    print("El número menor es: ", num1)
