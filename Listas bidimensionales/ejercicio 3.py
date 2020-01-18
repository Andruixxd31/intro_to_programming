def crea_Matriz3(n):
    matriz = []
    for ren in range(n):
        lista = []
        for num in range(n):
            lista.append(ren)
        matriz.append(lista)
    return matriz
