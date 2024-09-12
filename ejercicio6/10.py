#Escriba una función que tome un número como parámetro y verifique que el número sea primo o no.

n = int(input("ingrese un número "))

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
print(primo(n))
    