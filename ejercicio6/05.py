#Escriba un programa para invertir una cadena. Cadena de ejemplo: "1234abcd" Resultado esperado: "dcba4321"

def cadenai(cadena):
    return cadena[::-1]

inputcadena = "1234abcd"
inversa = cadenai(inputcadena)
print(inversa)