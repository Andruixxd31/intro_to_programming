"""
Andres Diaz de Leon
A01620020
"""
num = input("Introduzca un número >> ")
while not num.isnumeric():
    num = input("Introduzca un número >> ")
num = int(num)

cont = 1
factorial = num
while num != cont:
    factorial = factorial*cont
    cont += 1
print(factorial)