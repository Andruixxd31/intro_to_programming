"""
Ve cuantos digitos tiene un numero
Andrés Díaz de León
A01620020
"""
num = int(input("introduzca un numero enteroç: "))
dig = 1
while num >= 10 or num <= -10:
    dig += 1
    num = num//10

print(f"Ese número tiene {dig} digitos")

#Aprendi a ver como se desglosa un numero