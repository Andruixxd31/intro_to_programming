"""
Andrés Diaz de Leon
A01620020
EL usuario indica un numero de numeros a ingresar y se determina en que rango pertenece cada numero
"""

print("Hola buena persona, escriba una oracion o palabra por favor")
str = input(">>")
while not str.isprintable():
    print("Dato no valido")
    str = input(">>")
str = str.lower()
str = str.replace("e", "3")
str = str.replace("o", "h")
str = str.replace("a", "4")
for letter in str:
    print(letter)