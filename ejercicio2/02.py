#Preguntar al usuario el nombre y la edad, si es mayor o igual a 18 años mostrar el mensaje "Usted es mayor de edad", de lo contrario "Usted es menor de edad". Si el número ingresado es negativo o la edad ingresada es mayor a 100 años, mostrar al usuario un mensaje de ingresar una edad válida.

try:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    if edad < 0 or edad > 100:
        print("Ingrese una edad válida")
    elif edad >= 18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")
except ValueError:
  print("Error, por favor ingrese un número")