"""
Andres Diaz de Leon
A01620020
"""
print("¿Hasta cuantos kilometros desea ver la conversion?")
i = input(">>")

while not i.isnumeric():
    print("Dato no valido")
    i = input(">>")

i = int(i)
km = 1
m = 1.6
print("Kms      Millas")
while km <= i:
    print("%d        %5.2f"% (km, km*1.6))
    km += 1