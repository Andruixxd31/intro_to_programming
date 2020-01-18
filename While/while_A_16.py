"""
El programa genera un numero al azar y el usuario tiene 10 oportunidades para atinarle al numero
El programa indicara si le atino, es mayor o menor el número que hizo
Andrés Díaz de León
A01620020
"""
import random
num = random.randint(1,101) #Crea variable num con un mumero entre 1 y 100

print("Haremos un juego")
print("\t la computadora creará un número del 1 al 100")
print("\t\t Y tú trataras de atinarle al número en 7 intentos")
print("\t\t\t ¿Listo?")

contador = 1
while contador != 8:
    y = int(input(f"{contador}>> "))
    contador += 1
    if y > num:
        print(f"El numero es menor a {y}")
    elif y < num:
        print(f"El numero es mayor a {y}")
    else:
        print("¡GANASTE!")
        quit()
    if contador == 8:
        print("Suerte para la proxima")

#Aprendi a crear numeros aleatorios en python