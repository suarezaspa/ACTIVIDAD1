#Solicitar cinco (5) notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0. 

#ay no, desde aquí se pone complicado D:
# Solicitar cinco notas a un estudiante
notas = []
for i in range(5):
    nota = float(input(f"Nota {i+1}: "))
notas.append(nota)
# Calcular promedio
promedio = sum(notas) / len(notas)
# Mostrar resultado
if promedio >= 3.0:
    print("Aprobó")
else:
    print("No aprobó")
    #que curioso, cuando se suministran los números 4, 3, 3, 2, 2, aparece aprobado(no debería, pues 4+3+3+2+2=14) 
    # pero cuando se digitan otros números que también den 14, el estudiante no aprueba. no sé a qué se debe este error tan "curioso"
    #haciendo más pruebas, el órden no cambia. no importa como se sumisteren esos específicos números, siempre aprobará al estudiante. 
    #increíble
