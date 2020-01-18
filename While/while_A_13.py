"""
Programa que calcula volumen de 3 fuguras, da la opción de usarse más de una vez sin reiniciar el codigo
Andrés Díaz de León
A01620020
"""
import math
from math import *

resp = 0
while resp != 4:
    print("¿Que volumen desea encontar?")
    print("""
        [1] Cubo
        [2] Esfera 
        [3] Cono 
        [4] Salir 
        [cualquier otro numero] Quiero una sorpresa""")

    def cubo():
        lado = float(input("Cual es la longitud de los lados: "))
        volumen = lado ** 3
        print(f"lado: {lado}, volumen: {volumen} u^3")

    def esfera():
        radio = float(input("¿Cual es el radio?: "))
        volumen = pi*(4/3)*radio**3
        print(f"radio: {radio}, volumen: {volumen} u^3")

    def cono():
        radio = float(input("¿Cual es el radio?: "))
        h = float(input("¿Cual es la altura del cono?: "))
        volumen = (pi*radio**2*h)/3
        print(f"radio: {radio}, altura: {h}, volumen: {volumen} u^3")

    def sorpresa():
        print("""Esta sorpresa no hace nada
        XD
        """)

    resp = int(input("> "))
    if resp == 1:
        cubo()
    elif resp == 2:
        esfera()
    elif resp == 3:
        cono()
    elif resp == 4:
        print("Fin del programa")
        quit()
    else:
        sorpresa()

#Aprendí a usar funciones