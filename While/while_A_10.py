"""
Andrés Díaz de León
A01620020
"""

print("Ingrese un numero")
num = input(">>")
while not num.isnumeric():
    print("Dato no valido")
    num = input(">>")

num = int(num)
m = num/2
suma = 0
while m > 0:
    if num%m == 0:
        suma = suma + m
    m -= 1
if suma == num:
    print(f"{num} es un numero perfecto")