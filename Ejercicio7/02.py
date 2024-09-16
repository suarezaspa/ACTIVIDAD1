#Escriba una clase llamada Rectangle construida por una longitud y anchura y un método que calculará el área de un rectángulo.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
        
length = int(input("Ingrese la altura:"))
width = int(input("Ingrese la ancho:"))
rect = Rectangle(length, width)
print(f"El área del rectángulo es: {rect.area()}")