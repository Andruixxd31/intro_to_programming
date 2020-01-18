"""
Andrés Díaz de León
A01620020
"""
print("Tratare de adivinar un número, indicame si el número en tu cabeza es mayor o menor o si es el correcto :)")
valorMinimo = int(input("Valor minimo: "))
valorMaximo = int(input("Valor maximo: "))
adivinar = 0
resp = "no"

while resp != "si":
    adivinar = (valorMaximo+valorMinimo)//2
    print(f"¿El numero es {adivinar}?")
    resp = input(">>")
    resp = resp.lower()
    if resp == "mayor":
        valorMinimo = adivinar
    elif resp == "menor":
        valorMaximo = adivinar
    elif resp == "si":
        print("La computadora te gano XD")
    else:
        print("Respuesta no valida")
