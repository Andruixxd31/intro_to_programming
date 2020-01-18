"""
Andres Diaz de Leon
A016200020
Se escribe una oración y se muestra cuantos caracteres numericos se mostraron
"""
print("Howdy. Escribe una oración o te pego")
str = input(">>")

num = 0
for letra in str:
    if letra.isnumeric(): #Ve si un caracter es numerico o no
        num += 1 #Variable que matiene info de cuantos numeros se encuentran

print(f"Tu oración tiene {num} numeros")

print("-"*20)

cad= ["Hey", "hi", "5", "what is up!", "3", "7", "Xbox360", "amateur", "4eva"]

count = 0
for indice in cad:
    num = False
    for letra in indice:
        if letra.isnumeric() and num == False:
            count +=1
            num = True

print(f"De la lista {cad} {count} tienen carecteres numericos")
