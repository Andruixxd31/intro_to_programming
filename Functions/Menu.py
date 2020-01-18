""""
Andres Diaz de Leon
A01620020
El programa tiene un menu de selección que lleva a 3 funciones
a: Verifica que un dato numerico sea ingresado correctamente
"""
import random

def menu(): # Mi función prinicpal, invoca las demas funciones y crea un loop infinito
    while True:
        print("Seleccione una opción porfavor")
        print("[1]   energia")
        print("[2]   Encontrar multiplos comunes")
        print("[3]   Recargo de celular")
        print("[4]   Chiste al azar")
        print("[5]   Salir del programa")
        print("[<1 y >5]   Dibujo")
        op = input(">>")
        op = verificacion_num(op)

        if op == 1:
            E = energia()
            print(f"El resultado es {E}")
        elif op == 2:
            cont = multiplosComunes()
            print(f"Se encontraron {cont} multiplos comunes")
        elif op == 3: #Opción que crea un valor dentro de la condicional para pasar un parametro
            recargo = input(">>")
            recargo = verificacion_num(recargo)
            extra = llamadas(recargo)
            print(f"tienes  ahora {extra} dolares")
        elif op == 4:
            chiste()
        elif op == 5:
            quit()
        else:
            dibujo()


def energia():
    print("Ingrese la masa")
    masa = input(">>")
    masa = verificacion_num(masa)
    resultado= masa*90000000**2
    return resultado


def multiplosComunes():
    print("ingrese tres numeros. dos numeros para encontrar los multiple comunes de los 2 dentro del tercero")
    numeros = []
    for i in range(3): #agregar los numeros a una lista y hace que el usuario meta 3 valores
        x = input(">>")
        x = verificacion_num(x)
        numeros.append(x)
    multiplos = []
    cont = 0
    for x in range(1,numeros[2]+1): #Agrega
        if x%numeros[0] == 0 and x%numeros[1] == 0:
            cont += 1
            multiplos.append(x)
    print(multiplos)
    return cont

def llamadas(recargo):
    if recargo >= 5 and recargo <= 10:
        return 0 + recargo
    elif recargo == 25:
        return 3 + recargo
    elif recargo == 50:
        return 8 + recargo
    elif recargo == 100:
        return 20 + recargo

def chiste():
    x = random.randint(1,8)
    if x == 1:
        print("""¿Cuál fue el último animal en subir al arca de Noé? 
        Ed del-Fin"
        """)
    elif x == 2:
        print("""¿Cuál es el nombre del papá del Pato Donald? 
               Donal-berto"
               """)
    elif x == 3:
        print("""¿Cuál es el arbol mas terrorifico? 
                      EL bamboo"
                      """)
    elif x == 4:
        print("""¿Cómo se llama el hermano de Thor?
        Nillo""")
    elif x == 5:
        print("""¿Cuál es el lapiz que mata?
        LAPIZ-tola""")
    elif x == 6:
        print("""Intente ligar a una chava de informatica
               Pero no se de-JAVA""")
    elif x == 7:
        print("""Ayer me caí y pense que me habia roto el peroné
                     PeroNo""")


def dibujo(): #Simplemente imprime un dibujo
    print("""\t\t\t             .ed$$$$$eec.
       .e$$$$$$$$$$$$$$$$$$eeeee$$$$$c
      d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c
    .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $b
   d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F
  .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$**$ ^$$$$
 4 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*"     4$$F
 4 '$$$$$$$$$$$$$$$$$$$$$$$$$$$"        4$$
 4  $$$$$$$$$$$$$$$$$$$$$$$$$$$        .$$%
 d   $$$$$          $$$$$*$$$$$$c   ..e$$"
-    4$$$$          ^$$$$  *$$$$$F  ^\"\"\"
     4$$$$          4$$$$ z$$$$$"
     4$$$$          4$$$$ ^$$$P
     ^$$$$b         '$$$$e \n\n\n """)

def verificacion_num(num): #Verifica que los datos obtenidos sean numeros enteros positivos
    while not num.isnumeric():
        print("tu dato no es valido")
        num = input(">>")
    num = int(num)
    return num

menu()