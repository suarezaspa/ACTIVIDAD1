#Dada una lista de números. Escribe un programa para convertir cada elemento de una lista en su cuadrado. Ejemplo dado: numbers = [1, 2, 3, 4, 5, 6, 7]Resultado esperado: numbers = [1, 4, 9, 16, 25, 36, 49]

tales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tales = [i ** 2 for i in tales]
print(tales)