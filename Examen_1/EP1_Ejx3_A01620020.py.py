"""
Andrés Díaz de León
A01620020
Con la edad ve si puede entrar y si para entrar necesita un regalo
"""

print("Ingrese su edad")
edad = int(input(">> "))

if edad < 15:
    print("Acceso negado")
elif edad == 15:
    print("Acceso permitido")
else:
    print("Tiene un regalo")
    regalo = input(">> ")
    regalo = regalo.lower()  #Covierte el string a minisculas para que SI puede ser aceptado
    if regalo == "si":
        print("Acceso permitido")
    else:
        print("Acceso negado")