#Escriba un programa para mostrar n términos de número natural 
# y su suma (Fibonacci). Se le solicita al usuario que ingrese el n 
# término de la serie. Los primeros términos de la serie de Fibonacci son:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, y así sucesivamente.

n = int(input(f"Ingrese el número que quiera."))
r = range(1, n+1)
for n in r:
    print(n)

fib = [0, 1]
