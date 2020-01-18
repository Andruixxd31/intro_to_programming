"""
Andres diaz de Leon
A01620020
Ve si el numero de letras de las palabras de una lista es mayor a n
"""

def con_N_Letras(palabras, n): #Funcion
    cantidad = 0
    for indice in (palabras):
        if len(indice) >= n: #Se ve cada palabra y se saca cuandos caracteres tiene
            print(indice)
            cantidad += 1
    return cantidad

palabras = ["Hola", "Hello", "bonjour", "Hallo", "shalom", "hujambo", "merhaba", "Ciao", "welkom", "Que onda", "Buongiorno"]
print(len(palabras[0]))

print("dame un numero para ver cuantas palabras tienen mas o la misma catidad de letras del numero")
num = input(">>")
while not num.isnumeric():
    print("tu dato no es valido")
    num = input(">>")
num = int(num)

funcLetras = con_N_Letras(palabras, num)
print(f"Las palabra mostradas tiene igual a mas de {num} letras")