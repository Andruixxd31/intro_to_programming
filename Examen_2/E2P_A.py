
"""
Andrés Díaz de León
A01620020
"""
def restriccion(valores):
    minimo = min(valores) #función de una lista para encontrar el valor mas pequeño por magnitud
    return minimo


def validacion(x): #Función que solo acepta numeros positivos para que el usuaerio ni ingrese un caracter
    while not x.isnumeric():
        print("Dato no valido. Ingrese otro")
        x = input(">>")
    x = int(x)
    return x

print("Hola, porfavor mete 15 numeros enteros positivos porfavor")

numeros = []
for x in range(15): #Loop que hace que el usuario ingrese 15 valores
    n = input(">>")
    num = validacion(n)
    numeros.append(num)
print(numeros)

menor = restriccion(numeros)
print(f"El valor mas pequeño de la lista {numeros} es {menor}")





