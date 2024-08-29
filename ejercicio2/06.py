#Crear un programa con un menú de opciones, que permita calcular las áreas de figuras de rectangulo, cuadrado, paralelogramo, rombo, trapecio, triangulo, triangulo equilatero, triangulo rectangulo y polígono regular

import math

def calcular_area():
    print("1. Rectángulo")
    print("2. Cuadrado")
    print("3. Paralelogramo")
    print("4. Rombo")
    print("5. Trapecio")
    print("6. Triángulo")
    print("7. Triángulo equilátero")
    print("8. Triángulo rectángulo")
    print("9. Polígono regular")
    opcion = int(input("Ingrese el número de la figura que desea calcular: "))
    if opcion == 1:
        largo = float(input("Ingrese la longitud del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        area = largo * ancho
        print(f"El área del rectángulo es: {area}")
    elif opcion == 2:
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")
    elif opcion == 3:
        base = float(input("Ingrese la longitud de la base del paralelogramo: "))
        altura = float(input("Ingrese la altura del paralelogramo: "))
        area = base * altura
        print(f"El área del paralelogramo es: {area}")
    elif opcion == 4:
        diagonal1 = float(input("Ingrese la diagonal 1 del rombo: "))
        diagonal2 = float(input("Ingrese la diagonal 2 del rombo: "))
        area = (diagonal1 * diagonal2) / 2
        print(f"El área del rombo es: {area}")
    elif opcion == 5:
        base1 = float(input("Ingrese la longitud de la base 1 del trapecio: "))
        base2 = float(input("Ingrese la longitud 2 del trapecio: "))
        altura = float(input("Ingrese la altura del trapecio: "))
        area = ((base1 + base2) / 2) * altura
        print(f"El área del trapecio es: {area}")
    elif opcion == 6:
        base = float(input("Ingrese la longitud de la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif opcion == 7:
        lado = float(input("Ingrese la longitud del triángulo equilátero: "))
        area = (lado ** 2) * math.sqrt(3) / 4
        print(f"El área del triángulo equilátero es: {area}")
    elif opcion == 8:
        base = float(input("Ingrese la base del triángulo rectángulo: "))
        altura = float(input("Ingrese la altura del triángulo rectángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo rectángulo es: {area}")
    elif opcion == 9:
        lado = float(input("Ingrese el lado del polígono regular: "))
        num_lados = int(input("Ingrese el número de lados del polígono regular: "))
        area = (num_lados * lado ** 2) / (4 * math.tan(math.pi / num_lados))
        print(f"El área del polígono regular es: {area}")
    else:
        print("error")

calcular_area() #si así está el 6, no me imagino el 7 :skull