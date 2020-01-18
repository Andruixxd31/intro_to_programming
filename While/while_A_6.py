"""
Andres Diaz de Leon
A01620020
"""

print("Ingrese un numero")
num = input(">>")
while not num.isnumeric():
    print("Dato no valido")
    num = input(">>")

num = int(num)
i = 1
while i <= 10:
    print(f"{num} x {i}", num*i)
    i += 1