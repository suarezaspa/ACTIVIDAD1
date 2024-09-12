#Escriba una función que acepte una cadena y calcule el número de letras mayúsculas y minúsculas. 

cadena = input("ingrese la cadena: ")

def contar_letras(cadena):
    mayusculas = 0
    minusculas = 0
    for letra in cadena:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
                minusculas += 1
    return mayusculas, minusculas

mayusculas, minusculas = contar_letras(cadena)
print(f"Mayúsculas: {mayusculas}, Minúsculas: {minusculas}")
