#Contar el número de ocurrencias del elemento 50 en una tupla

tuple1 = (50, 10, 60, 70, 50)
cont = 0
for i in tuple1:
    if i == 50:
        cont += 1
print(cont)