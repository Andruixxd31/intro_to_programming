"""
Andrés Díaz de León
A01620020
"""
from math import *



def validacion(x): #Función que solo acepta numeros positivos para que el usuaerio ni ingrese un caracter
    while not x.isnumeric():
        print("Dato no valido. Ingrese otro")
        x = input(">>")
    x = int(x)
    return x

def multiplos(listaParaComparar):
    num = 3
    listaDeMultiplos = []
    for i in listaParaComparar:
        if i%num == 0:
            listaDeMultiplos.append(i)
    return listaDeMultiplos

def perimetroDelTriangulo(coord): #Para pasar los valores en un argumento hice una lista
    distanciaAB = sqrt((coord[2] - coord[0])**2 + (coord[3] - coord[1])**2)
    distanciaAC = sqrt((coord[4] - coord[0]) ** 2 + (coord[5] - coord[1]) ** 2)
    distanciaBC = sqrt((coord[4] - coord[2]) ** 2 + (coord[5] - coord[3]) ** 2)
    distanciaTotal = distanciaAB + distanciaAC + distanciaBC
    return distanciaTotal

def coordenadas():
    coord = []
    print("Ingresa las coordenadas")
    for i in range(6):
        num = input(">>")
        num = validacion(num)
        coord.append(num)
        print(coord)
    perimetro = perimetroDelTriangulo(coord)
    return perimetro

def triangulo():
    perimetro = coordenadas() #Función que invocara a la siguiente funcion patra al final regresar el perimetro
    return perimetro

def opciones():
    op = input(">>")
    option = validacion(op)

    if option == 1:
        numerosParaComparar = [34,276,27,2,1,96,3,78,900,32,1998,3,100000]
        nuevaLista = multiplos(numerosParaComparar)
        print(f"de la lista {numerosParaComparar} estos son multiples de 3 {nuevaLista}\n")
    elif option == 2:
        perimetro = triangulo()
        print(f"El perimetro mide {perimetro}")
    else:
        quit()


while True: #Loop que será infinito al menos que se indica al programa a salir con quit()
    print("[1]\t\t\t\tMultiplos de")
    print("[2]\t\t\t\tTriangulo")
    print("[otro numero]\tSalir")
    print("\n")
    opciones() #Se hizo otra funicón para tener mas simple el menu