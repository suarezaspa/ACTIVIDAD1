#Escriba una función que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista. 

def elementos(lista):
    return list(set(lista))

print(elementos([1, 2, 2, 3, 4, 4]))
