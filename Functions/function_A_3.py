"""
Andres diaz de Leon
A01620020
El usuario escribe una letra de esa lista se va las palabras que incia con esa letra
"""

def empiezan_Con(lista, caracter):
    total = 0
    for palabra in lista:
        if caracter == palabra[0]:
            print(palabra)
            total += 1
    return total

lyrics = """So, so you think you can tell
Heaven from Hell
Blue skies from pain
Can you tell a green field
From a cold steel rail
A smile from a veil
Do you think you can tell?
And did they get you to trade
Your heroes for ghosts
Hot ashes for trees
Hot air for a cool breeze
Cold comfort for change
And did you exchange
A walk on part in the war
For a leading role in a cage?
"""

lyrics = lyrics.lower()
lyrics = lyrics.split()

print("Escriba una lera porfavor")
letra = input(">>")
while not letra.isalpha():
    print("Esa no es una letra, ponga una letra porfa")
    letra = input(">>")
letra = letra.lower()

total = empiezan_Con(lyrics, letra)
print(f"En total {total} palabra inician con {letra}")
