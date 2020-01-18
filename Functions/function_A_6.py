"""
Andres Diaz de Leon
A01620020
"""

def vocales_Mayusculas(string):
    vocales = ["a", "e", "i", "o", "u"]
    i = 0
    for letra in string:
        if letra in vocales:
            letra = vocales[i]
            letra = letra.upper()
            string.insert(i, letra)
    i += 1
    return string



oracion = "hola como estas?"
nuevaOracion = list(oracion)
nuevaOracion = vocales_Mayusculas(oracion)


