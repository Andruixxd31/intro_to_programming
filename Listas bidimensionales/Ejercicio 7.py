Listas = [[1,-3,5,2,7,-3,8,3,-3,4], [-454,45,27,8,6,-35,12], [32,-535,-356,21,-64,7549]]


def postivos_listas(Listas):
    print(Listas)
    positivos = 0
    for lista in Listas:
        for elemento in lista:
            if elemento > 0:
                positivos += 1
    return positivos

resultado = postivos_listas(Listas)
print(f"Estos son los positvos {resultado}")

