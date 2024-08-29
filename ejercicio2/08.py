#Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente.

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 < n2 and n1 < n3:
    if n2 < n3:
        ascendente = (n1, n2, n3)
        descendente = (n3, n2, n1)
    else:
        ascendente = (n1, n3, n2)
        descendente = (n2, n3, n1)
elif n2 < n1 and n2 < n3:
    if n1 < n3:
        ascendente = (n2, n1, n3)
        descendente = (n3, n1, n2)
    else:
        ascendente = (n2, n3, n1)
        descendente = (n1, n3, n2)
elif n3 < n1 and n3 < n2:
    if n1 < n2:
        ascendente = (n3, n1, n2)
        descendente = (n2, n1, n3)
    else:
        ascendente = (n3, n2, n1)
        descendente = (n1, n2, n3)
else:
    ascendente = (n1, n1, n1)
    descendente = (n1, n1, n1)

print("Orden ascendente:", ascendente)
print("Orden descendente:", descendente) #este funciona sin "problemas"