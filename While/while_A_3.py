"""
Andres Diaz de Leon
A01620020
"""
p = ">>"

valid = False
print("Ingrese el capital inicial")
capital = input(p)
while not valid:
    if not capital.isnumeric():
        print("Dato no valido")
        capital = input(p)
    else:
        capital = float(capital)
        valid = True

doble = capital*2

valid = False
print("Ingrese el interes")
interes = input(p)
while not valid:
    if not interes.isnumeric():
        print("Dato no valido")
        interes = input(p)
    else:
        interes = float(interes)
        interes = interes/100+1
        print(interes)
        valid = True

anios = 0
while capital < doble:
    capital = capital*interes
    anios += 1
if anios > 1:
    print(f"EL capital se duplicaria en {anios} años")
else:
    print("EL capital se duplicaria en un año")