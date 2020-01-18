decenas = [10,20,30,40]
print(decenas[1:3])
print(decenas[:3])
print(decenas[:3:2])
print(decenas[3::-1])
print(decenas[::-1])
print(decenas[2::-1])
print(len(decenas))
print(max(decenas))
print(min(decenas))
print(sum(decenas))

cadena = "Muy facil programar en python"

for indice in range(len(cadena)):
    print("letra {0:2d}: {1}".format(indice, cadena[indice]))

"""
El {1} me imprime los caracteres si se usa {0} se imprimen la indexación de las letras
indice imprime la indexacion de la letras para mostrar su lugar en el string
cadena[indice] obtiene los caracteres del string por su posición
"""
