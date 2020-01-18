
"""
Andrés Díaz de León
A01620020
"""

def crea_Matriz1(n):
    matriz=[[-1]*n]*n
    return matriz

def crea_Matriz2(n):
    lista = []
    for num in range(n):
        lista.append(num)
    matriz = [[lista]] * n
    return matriz

def crea_Matriz3(n):
    matriz = []
    for ren in range(n):
        lista = []
        for num in range(n):
            lista.append(ren)
        matriz.append(lista)
    return matriz

def creamatriz4(n):
    return [list(range(x+1, (n ** 2) + 1, n)) for x in range(n)]

def cuentaPares():
    pares = 0
    for lista in Listas:
        for elemento in lista:
            if elemento%2 == 0:
                pares += 1
    return pares

def sumaMatriz(listas):
    listas = sum(map(sum, listas))
    return listas

def cambiaNegativos(listas):
    for lista in listas:
        x = [num * 0 if num < 0 else num for num in lista]
        return x

def cuentaRepeticiones(Listas):
    cuenta = 0
    n = -3
    for lista in Listas:
        for elemento in lista:
            if elemento == n:
                cuenta += 1
    return cuenta

def busca(listas, x):
    for lista in listas:
        for elemento in lista:
            if elemento == x:
                return True
    return False

def sumaMayores5(listas):
    suma = 0
    for lista in listas:
        for elemento in lista:
            if elemento > 5:
                suma += elemento
    return suma

def cambia_ceros(listaA):
    for ren in range(len(listaA)):
        for col in range(len(listaA[ren])):
            if listaA[ren][col] == 0:
                listaA[ren][col] = ren + col
    return listaA

