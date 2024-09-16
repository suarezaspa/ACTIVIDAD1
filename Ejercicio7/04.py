#Escriba una clase para implementar pow(x, n).

class Pow:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return x * self.myPow(x * x, n // 2)

x = int(input("ingrese el valor de x"))
n = int(input("ingrese el valor de n"))
obj = Pow()
print(obj.myPow(x, n))
