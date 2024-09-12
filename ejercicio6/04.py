#Escriba una función para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336

tal = [8, 2, 3, -1, 7]
def multiplicar_numeros(tal):
    resultado = 1
    for i in tal:
        resultado *= i
    return resultado

final = multiplicar_numeros(tal)
print(final)