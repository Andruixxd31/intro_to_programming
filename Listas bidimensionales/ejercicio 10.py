listas = [[1,3,5,2,7,3,8], [4,4,2,8,6,3,1], [3,5,3,2,6,7]]

def busca(listas, x):
    for lista in listas:
        for elemento in lista:
            if elemento == x:
                return True
    return False