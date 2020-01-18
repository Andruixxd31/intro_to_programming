"""
Andres diaz de Leon
A01620020
compara un numero con los elementos d euna lista
"""

def mayores_N(lista, numero):
    mas = 0
    for i in lista:
        if i < numero: #se empieza desde el indice 0
             mas += 1
    return mas #mi valor numerico de veces que el valor fue mayor a los valores de la lista 

unoAlNueve = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = input(">>")
while not num.isnumeric():
    print("Dato no valido")
    num = input(">>")
num = int(num)

comp = mayores_N(unoAlNueve, num)
print(f"{num} es mayor a {comp} elemento de la lista")