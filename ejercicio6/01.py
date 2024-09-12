#Escriba una función para encontrar el máximo de tres números. 

def papu():
    n1 = int(input("ingrese el primer numero: "))
    n2 = int(input("ingrese el segundo numero: "))
    n3 = int(input("ingrese el tercero numero: "))
    if n1 > n2 and n1 > n3:
        print("el numero mayor es: ",n1)
    elif n2 > n1 and n2 > n3:
        print("el numero mayor es: ",n2)
    elif n3 > n1 and n3 > n2:
        print("el numero mayor es: ",n3)
    else:
        print("error")

papu()