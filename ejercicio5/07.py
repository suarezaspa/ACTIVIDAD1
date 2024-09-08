#Ordenar una tupla de tuplas por el segundo elemento

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

for i in range(len(tuple1)):
    for j in range(i + 1, len(tuple1)):
        if tuple1[i][1] > tuple1[j][1]:
            tuple1 = tuple1[:i] + (tuple1[j],) + tuple1[i+1:j] + (tuple1[i],) + tuple1[j+1:]

print(tuple1) #es demasiado complejo, pero funciona(creo)