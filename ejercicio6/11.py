#Escriba un programa para imprimir los números pares de una lista determinada.

tal = [1, 2, 3, 4, 5, 6, 7]

def impripares(tal):
    for i in tal:
        if i % 2 == 0:
            print(i)

impripares(tal)
