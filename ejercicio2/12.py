#Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay descuento. Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%. Si compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y el valor del precio unitario original. Calcule y muestre el valor total a pagar.

cant = int(input("Ingrese la cantidad de artículos: "))
precio = float(input("Ingrese el precio unitario: $"))

if cant <= 5:
    valor_total = cant * precio
elif 5 < cant < 10:
    descuento = precio * 0.05
    precio_descuento = precio - descuento
    valor_total = cant * precio_descuento
else:
    descuento = precio * 0.08
    precio_descuento = precio - descuento
    valor_total = cant * precio_descuento

print(f"El valor total a pagar es: ${valor_total:.2f}")
