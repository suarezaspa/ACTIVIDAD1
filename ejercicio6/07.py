#Escriba una función para comprobar si un número cae en un rango determinado. Defina como parámetros rango de inicio, número y rango final.  

def dentro_rango(inicio, numero, fin):
    return inicio <= numero <= fin
inicio_rango = 50
fin_rango = 150
numero_a_comprobar = 100

if dentro_rango(inicio_rango, numero_a_comprobar, fin_rango):
    print(f"{numero_a_comprobar} está dentro del rango [{inicio_rango}, {fin_rango}]")
else:
    print(f"{numero_a_comprobar} no está dentro del rango [{inicio_rango}, {fin_rango}]")