#Escriba un programa para calcular el factorial de un número dado.

n = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("El factorial del número ingresado es: ", factorial) #usar un tabulador al principio de esta línea da todos los factoriales hasta el número solicitado.
