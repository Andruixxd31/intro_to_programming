listas = [[1,-3,5,2,7,-3,8,3,-3,4], [-454,-3,27,8,6,-3,12], [32,-535,-3,21,-64,7549]]

def cuentaRepeticiones(Listas):
    cuenta = 0
    n = -3
    for lista in Listas:
        for elemento in lista:
            if elemento == n:
                cuenta += 1
    return cuenta
