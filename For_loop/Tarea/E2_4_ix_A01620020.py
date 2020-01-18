"""
Andres Diaz de Leon
A016200020
Se escribe una oración y se muestra cuantos caracteres numericos se mostraron
"""

miLista = []
print("Ingrese lo que quiera 10 veces amig@ mio")
for i in range(10):
    cad = input(">>")
    cad = cad.upper()
    miLista.append(cad)

print(f"Aquis esta tu lista pero en mayusculas: {miLista}")
