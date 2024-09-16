#Escriba una clase llamada Circle construida por un radio y dos métodos que calcularán el área y el perímetro de un círculo.

class Circle:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * (self.radio ** 2)
    def circumferencia(self):
        return 2 * 3.14 * self.radio

radio = int(input("Ingrese la medad del radio:"))
circle = Circle(radio)
print("El área del círculo es:", circle.area())
print("El perímetro del círculo es:", circle.circumferencia())
