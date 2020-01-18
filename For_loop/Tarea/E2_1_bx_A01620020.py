"""
Andres Diaz de Leon
A01620020
Programa que consigue 3 calificaciones de 3 alumnos para ver el promedio de cada uno
"""
i = x = 1
suma = 0
for i in range(1,4):
    for x in range(1,4): #se usa for loops anidados para que el proceso se repita tres veces al correrlo una vez
        print(f"Ingrese la calificación:")
        calificacion = float(input(f"[{x}]>>")) #Indica que calificación se mete
        suma += calificacion
        promedio = suma/x #Saca el promedio al usar el valor de x en el for loop
    print(f"La promedio del estudiante {i} es de {promedio}")
    calificacion = suma = 0