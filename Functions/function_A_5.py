"""
Andres diaz de Leon
A01620020
El usuario escribe una letra de esa lista se va las palabras que incia con esa letra
"""

def locura(stringAModificar):
    stringLoco = stringAModificar.replace("e", "3").replace("o", "h").replace("a", "4")
    return stringLoco


print("Ingresa una palabra o frase porfavor")
stringOrginal = input(">>")
stringLoco = locura(stringOrginal)
print(f"Tu frase al entrar al manicomio se ve asi: {stringLoco}")
