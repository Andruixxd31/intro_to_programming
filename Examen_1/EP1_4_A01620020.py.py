"""
Andrés Díaz de León
A01620020
"""
print("Ingrese 20 números o me enojo")
cont = 1 #La variable que hara repitir el loop 20 veces
negativos = 0
positivos = 0
while cont <= 20:
    num = float(input(f"{cont}>> "))
    cont += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print("Cantidad de negativos:", negativos)
print("Cantidad de positivos:", positivos)
