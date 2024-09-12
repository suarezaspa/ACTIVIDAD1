#Escriba una función para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.

n = int(input("Ingrese el número del que quiere ver su factorial"))

def factorial(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))