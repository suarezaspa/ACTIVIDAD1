#Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona que se calcula con la fórmula IMC=P/(E*E) en donde P es el peso en Kg. y E es la estatura en metros. Lea un valor de P y de E, calcule el IMC y muestre su estado según la siguiente tabla:
#aquí iría la susodicha tabla pero me dió pereza transcribirla. mala mía 

def calcular_imc(p, e):
  imc = p / (e ** 2)
  return imc

m = float(input("Ingrese su peso en kg: "))
h = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(m, h)

print("Su IMC es: ", imc)

if imc < 18.5:
  print("Usted está desnutrido")
elif 18.5 <= imc < 24.9:
  print("Usted tiene un peso normal")
elif 25 <= imc < 29.9:
  print("Usted tiene sobrepeso")
elif 30 <= imc < 34.9:
  print("Usted tiene obesidad tipo 1")
elif 35 <= imc < 39.9:
  print("Usted tiene obesidad tipo 2")
elif 40 <= imc < 49.9:
  print("Usted tiene obesidad tipo 3")
else:
  print("Usted tiene obesidad tipo 4")