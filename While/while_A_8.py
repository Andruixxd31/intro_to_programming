"""
Andrés Díaz de León
A01620020
"""
i = input("Cuantos numero quiere ingresar: ")
while not i.isnumeric():
    print("NO")
    i = input(">>")
i = int(i)
negativos = 0
positivos = 0

cont = 1
while cont <= i:
    num = float(input(f"{cont}>> "))
    cont += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print("Cantidad de negativos:", negativos)
print("Cantidad de positivos:", positivos)