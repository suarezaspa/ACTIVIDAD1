#Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área. 

import math

def area_rectángulo(longitud, ancho):
    return longitud * ancho

def area_cuadrado(longitud):
    return longitud ** 2

def area_paralelogramo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_trapecio(base1, base2, altura):
    return (base1 + base2) * altura / 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_triangulo_equilátero(longitud):
    return (longitud ** 2) * (3 ** 0.5) / 4

def area_triangulo_rectángulo(base, altura):
    return (base * altura) / 2

def area_poligono_regular(numero_lados, longitud):
    return (numero_lados * (longitud ** 2)) / (4 * math.tan(math.pi / numero_lados))

print("1. Rectángulo")
print("2. Cuadrado")
print("3. Paralelogramo")
print("4. Rombo")
print("5. Trapecio")
print("6. Triángulo")
print("7. Triángulo equilátero")
print("8. Triángulo rectángulo")
print("9. Polígono regular")

figura = int(input("Ingrese el número de la figura que desea calcular: "))

if figura == 1:
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    área = area_rectángulo(longitud, ancho)
    print(f"El área del rectángulo es: {área:.2f}")
elif figura == 2:
    longitud = float(input("Ingrese la longitud del cuadrado: "))
    área = area_cuadrado(longitud)
    print(f"El área del cuadrado es: {área:.2f}")

elif figura == 3:
    base = float(input("Ingrese la base del paralelogramo: "))
    altura = float(input("Ingrese la altura del paralelogramo: "))
    área = area_paralelogramo(base, altura)
    print(f"El área del paralelogramo es: {área:.2f}")

elif figura == 4:
    diagonal1 = float(input("Ingrese la diagonal 1 del rombo: "))
    diagonal2 = float(input("Ingrese la diagonal 2 del rombo: "))
    área = area_rombo(diagonal1, diagonal2)
    print(f"El área del rombo es: {área:.2f}")

elif figura == 5:
    base1 = float(input("Ingrese la base 1 del trapecio: "))
    base2 = float(input("Ingrese la base 2 del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    área = area_trapecio(base1, base2, altura)
    print(f"El área del trapecio es: {área:.2f}")

elif figura == 6:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    área = area_triangulo(base, altura)
    print(f"El área del triángulo es: {área:.2f}")

elif figura == 7:
    longitud = float(input("Ingrese la longitud del triángulo equilátero: "))
    área = area_triangulo_equilátero(longitud)
    print(f"El área del triángulo equilátero es: {área:.2f}")

elif figura == 8:
    base = float(input("Ingrese la base del triángulo rectángulo: "))
    altura = float(input("Ingrese la altura del triángulo rectángulo: "))
    área = area_triangulo_rectángulo(base, altura)
    print(f"El área del triángulo rectángulo es: {área:.2f}")

elif figura == 9:
    numero_lados = int(input("Ingrese el número de lados del polígono regular: "))
    longitud = float(input("Ingrese la longitud del lado del polígono regular: "))
    área = area_poligono_regular(numero_lados, longitud)
    print(f"El área del polígono regular es: {área:.2f}")

else:
    print("error")