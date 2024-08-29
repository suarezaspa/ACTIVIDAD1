#Programa que permita a un usuario tomar una decisión del tipo de pago a usar. Si la cuenta es menor a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 pago con el celular (dinero electrónico). Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Todos los valores superiores a $6000000, pago con la tarjeta de crédito.

def pago():
    print("¿Cómo deseas pagar?")
    print("1. Efectivo")
    print("2. Dinero electrónico")
    print("3. Tarjeta de débito")
    print("4. Tarjeta de crédito")
    opcion = input("Ingrese el número de la opción de pago que desea realizar: ")
    if opcion == "1":
        monto = float(input("Ingrese el monto de la cuenta: "))
        if monto < 150000:
            print("El pago se realizará en efectivo.")
        else:
            print("El pago no se realizará en efectivo.")
    elif opcion == "2":
        monto = float(input("Ingrese el monto de la cuenta: "))
        if 150000 <= monto <= 300000:
            print("El pago se realizará con el dinero electrónico.")
        else:
            print("El pago no se realizará con el dinero electrónico.")
    elif opcion == "3":
        monto = float(input("Ingrese el monto de la cuenta: "))
        if 300000 < monto <= 600000:
            print("El pago se realizará con la tarjeta de débito.")
        else:
            print("El pago no se realizará con la tarjeta de débito.")
    elif opcion == "4":
        monto = float(input("Ingrese el monto de la cuenta: "))
        if monto > 600000:
            print("El pago se realizará con la tarjeta de crédito.")
        else:
            print("El pago no se realizará con la tarjeta de crédito.")
    else:
        print("Error: No se ha seleccionado una opción de pago válida.")
pago()