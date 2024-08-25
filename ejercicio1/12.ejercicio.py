
c1 = float(input("Ingrese la longitud de un cateto: "))
c2 = float(input("Ingrese la longitud del otro cateto: "))

h2 = c1 * c1 + c2 * c2

aproximacion = h2 / 2.0
                                     #if it ain´t broke, don´t fix it 
for i in range(20):  
    aproximacion = (aproximacion + h2 / aproximacion) / 2

h = aproximacion

print(f"La hipotenusa es aproximadamente: {h}")
