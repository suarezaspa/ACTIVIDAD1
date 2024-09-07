#Eliminar cadenas vacías de la lista de cadenas. Ejemplo dado: list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]Resultado esperado: ["Mike", "Emma", "Kelly", "Brad"]

tales = ["sandía", "uva", "", "", "pera", "", "manzana", "", 7]
tales = [i for i in tales if i != ""]
print(tales)
