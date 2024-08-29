#Conversión de temperaturas. Crear un menú de opciones. 

def cambios():
    print("1. Celcius a Farenheit")
    print("2. Celcius a Kelvin")
    print("3. Celcius a Rankie")
    print("4. Celcius a Réaumur")
    print("5. Farenheit a Celcius")
    print("6. Farenheit a Kelvin")
    print("7. Farenheit a Rankie")
    print("8. Farenheit a Réaumur")
    print("9. Kelvin a Celcius")
    print("10. Kelvin a Farenheit")
    print("11. Kelvin a Rankie")
    print("12. Kelvin a Réaumur")
    print("13. Rankie a Celcius")
    print("14. Rankie a Farenheit")
    print("15. Rankie a Kelvin")
    print("16. Rankie a Réaumur")
    print("17. Réaumur a Celcius")
    print("18. Réaumur a Farenheit")
    print("19. Réaumur a Kelvin")
    print("20. Réaumur a Rankie")
    opcion = int(input("Ingrese la opción que desee: "))

    if opcion == 1:
        c = float(input("Ingrese la temperatura en Celcius: "))
        f = c * 9/5 + 32
        print(f"La temperatura en Farenheit es: {f}")
    elif opcion == 2:
        c = float(input("Ingrese la temperatura en Celcius: "))
        k = c + 273.15
        print(f"La temperatura en Kelvin es: {k}")
    elif opcion == 3:
        c = float(input("Ingrese la temperatura en Celcius: "))
        r = c * 1.8 + 32
        print(f"La temperatura en Rankie es: {r}")
    elif opcion == 4:
        c = float(input("Ingrese la temperatura en Celcius: "))
        r = c * 0.8
        print(f"La temperatura en Réaumur es: {r}")
    elif opcion == 5:
        f = float(input("Ingrese la temperatura en Farenheit: "))
        c = (f - 32) * 5/9
        print(f"La temperatura en Celcius es: {c}")
    elif opcion == 6:
        f = float(input("Ingrese la temperatura en Farenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print(f"La temperatura en Kelvin es: {k}")
    elif opcion == 7:
        f = float(input("Ingrese la temperatura en Farenheit: "))
        r = (f - 32) * 5/9 * 1.8 + 32
        print(f"La temperatura en Rankie es: {r}")
    elif opcion == 8:
        f = float(input("Ingrese la temperatura en Farenheit: "))
        r = (f - 32) * 5/9 * 0.8
        print(f"La temperatura en Réaumur es: {r}")
    elif opcion == 9:
        k = float(input("Ingrese la temperatura en Kelvin: "))
        c = k - 273.15
        print(f"La temperatura en Celcius es: {c}")
    elif opcion == 10:
        k = float(input("Ingrese la temperatura en Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print(f"La temperatura en Farenheit es: {f}")
    elif opcion == 11:
        k = float(input("Ingrese la temperatura en Kelvin: "))
        r = (k - 273.15) * 1.8 + 32
        print(f"La temperatura en Rankie es: {r}")
    elif opcion == 12:
        k = float(input("Ingrese la temperatura en Kelvin: "))
        r = (k - 273.15) * 0.8
        print(f"La temperatura en Réaumur es: {r}")
    elif opcion == 13:
        r = float(input("Ingrese la temperatura en Rankie: "))
        c = (r - 32) / 1.8
        print(f"La temperatura en Celcius es: {c}")
    elif opcion == 14:
        r = float(input("Ingrese la temperatura en Rankie: "))
        f = (r - 32) / 1.8 * 9/5 + 32
        print(f"La temperatura en Farenheit es: {f}")
    elif opcion == 15:
        r = float(input("Ingrese la temperatura en Rankie: "))
        k = (r - 32) / 1.8 + 273.15
        print(f"La temperatura en Kelvin es: {k}")
    elif opcion == 16:
        r = float(input("Ingrese la temperatura en Rankie: "))
        re = (r - 32) / 1.8 * 0.8
        print(f"La temperatura en Réaumur es: {re}")
    elif opcion == 17:
        re = float(input("Ingrese la temperatura en Réaumur: "))
        c = re / 0.8
        print(f"La temperatura en Celcius es: {c}")
    elif opcion == 18:
        re = float(input("Ingrese la temperatura en Réaumur: "))
        f = re / 0.8 * 9/5 + 32
        print(f"La temperatura en Farenheit es: {f}")
    elif opcion == 19:
        re = float(input("Ingrese la temperatura en Réaumur: "))
        k = re / 0.8 + 273.15
        print(f"La temperatura en Kelvin es: {k}")
    elif opcion == 20:
        re = float(input("Ingrese la temperatura en Réaumur: "))
        r = re / 0.8 * 1.8 + 32
        print(f"La temperatura en Rankie es: {r}")
    else:
        print("Opción inválida. Intente de nuevo.")

cambios() #:(