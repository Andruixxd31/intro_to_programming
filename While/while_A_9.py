"""
Andrés Díaz de León
A01620020
"""

i = input("Cuantos numero quiere ingresar: ")
while not i.isnumeric():
    print("NO")
    i = input(">>")
i = int(i)

cont = 1
multiplos = 0
while cont <= i:
    num = input(f"{cont}>> ")
    cont += 1
    if num == ".":
        break
    else:
        num = int(num)
        if num%i == 0:
            multiplos += 1
if multiplos != 0:
    if multiplos > 1:
        print(f"{multiplos} valores ingresado fueron multiplos de {i}")
    else:
        print("Un valor ingresado fue multiplo de ", i)