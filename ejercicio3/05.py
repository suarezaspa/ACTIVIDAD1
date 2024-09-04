#Escriba un programa para mostrar la tabla de multiplicar de un entero dado.

n = int(input("Ingrese un número para mostrar sus primeras diez tablas de multiplicar"))
r = range(1, 11)

for i in r:
    multer = n * i
    print(f"{n} * {i} = {multer}")