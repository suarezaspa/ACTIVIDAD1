#Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como:
#*
#**
#***
#****
#*****
#****
#***
#**
#*
#nada de funciones. solo ciclos.
aster = 5
for i in range(1, aster+1):
    print("*" * i)
for i in range(aster-1, 0, -1):
    print("*" * i)
