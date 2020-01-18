"""
Andrés Díaz de León
A01620020
Se usa la secuencia de Siracusa
"""

valid = False
while not valid:
    print("Introduzca un numero positivo porfavor")
    num = input(">>")
    if not num.isdigit():
        print("Porfavor no sea chistoso")
        continue
    else:
        print("Gracias por su numero")
    num = int(num)
    while num != 1:
        if num % 2 == 0:
            num = num/2
            print(num)
        else:
            num = 3*num + 1
            print(num)
        valid = True
print("Adios")