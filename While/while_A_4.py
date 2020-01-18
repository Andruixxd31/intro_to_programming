"""
Andrés Díaz de León
A01620020
Programa que verifica la entrada de valores del 1 al 10
"""

valid = False
print("Escriba un numero del 1 al 10")
num = input(">>")


while not valid:
    if not num.isdigit():
        print("Su dato no es numero positivo")
        print("Escriba un numero del 1 al 10")
        num = input(">>")
    else:
        num = int(num)
        if num < 0 or num > 10:
            print("Numero fuera del rango")
            num = input(">>")
        else:
            print("Gracias")
            valid = True

#Aprendi a validar datos y alternativas a la función continue