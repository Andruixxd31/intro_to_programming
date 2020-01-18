"""
Andrés Diaz de Leon
A01620020
EL usuario indica un numero de numeros a ingresar y se determina en que rango pertenece cada numero
"""

print("¿Cuantos numeros deasea ingresar? Los numeros solo son enteros")
numeros = input(">>")
while not numeros.isnumeric(): #Verificación de un número entero positivo
    print("dato no valido")
    numeros = input(">>")
numeros = int(numeros)

menos = mas = entre = 0
for x in range(1, numeros+1):
    num = input(f"{x}>>")
    Nnum = num
    Nnum = int(Nnum) #variable de un numero negativo para que su valor se pueda comparar en los if's
    num = num.lstrip("-")#Elimina el guion para que el dato sea valido
    while not num.isnumeric():
        print("dato no valido")
        num = input(">>")
    num = int(num)
    if num <= -5 or Nnum <= -5:
        menos += 1
    elif num >= 5 or Nnum >= 5:
        mas += 1
    else:
        entre += 1

print(f"hay {menos} numeros menores o iguales a -5")
print(f"hay {mas} numeros mayores o iguales a 5")
print(f"hay {entre} numeros entre -5 y 5")