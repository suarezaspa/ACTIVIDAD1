#Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.

n = 0
suma = 0
promedio = 0
while n < 10:
    num = int(input("Ingrese un número: "))
    suma = suma + num
    n = n + 1
    print("La suma de los números es: ", suma)
    promedio = suma / 10
    print("El promedio de los números es: ", promedio) #creo que está mal xd