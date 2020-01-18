"""
Obtiene una cantidad de número enteros hasta que se ingrese un negativo
Al final da la suma y el promedio y cúal fue el mayor número que se dio
Andrés Díaz de León
A01620020
"""

print("Ingrese los números postivos enteros que quiera, cuando acabe ponga uno negativo:")
num = max = sum = cont = 0
while num >= 0:
    num = int(input(">>"))
    if num >= 0:
        sum = sum + num
        cont += 1
    else:
        print("fin del programa")
    if num > max:
        max = num

print(f"el numero mayor fue {max}")
print(f"La suma es equialente a {sum}")
promedio = sum/cont
print(f"El promedio es {promedio}")