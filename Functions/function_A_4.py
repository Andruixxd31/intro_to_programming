"""
Andres diaz de Leon
A01620020
El usuario escribe una letra de esa lista se va las palabras que incia con esa letra
"""

def duplica(oneFold):
    twoFold = []
    for num in oneFold:
        num *= 2
        twoFold.append(num)
    return twoFold



misNumeros = [2.3, 5,3, 8, .2, 5, 10]
susNumeros = duplica(misNumeros)

print(f"La lista con los numeros originales: {misNumeros}")
print(f"La lista con los numeros duplicados: {susNumeros}")