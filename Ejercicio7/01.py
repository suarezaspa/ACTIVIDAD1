#Escriba una clase que represente un vehículo con métodos y atributos. Dentro atributos cree uno llamado “placa” y en los métodos cree uno que permita determinar de acuerdo con el día (datetime), si el vehículo tiene restricción por pico y placa o no, en la ciudad de Bogotá. 

from datetime import datetime

class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    def tiene_restriccion(self, fecha: datetime) -> bool:
        if fecha.weekday() == 6:
            return False
        elif fecha.weekday() % 2 == 0:
            ultimo_digito_placa = int(self.placa[-1])
            if ultimo_digito_placa in [6, 7, 8, 9, 0]:
                return False
            else:
                return True
        else:  
            ultimo_digito_placa = int(self.placa[-1])
            if ultimo_digito_placa in [1, 2, 3, 4, 5]:
                return True
            else:
                return False

vehiculo = Vehiculo("ZAP666", "Dodge", "Challenger")
fecha = datetime.now()
if vehiculo.tiene_restriccion(fecha):
    print("El vehículo tiene restricción")
else:
    print("El vehículo no tiene restricción")
                