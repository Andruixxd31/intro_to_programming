numeros = [[1,0,5,2,7,-3], [-454,45,27,8,6,0], [0,-535,-356,21,-64,7549]]


def cambia_ceros(listaA):
    for ren in range(len(listaA)):
        for col in range(len(listaA[ren])):
            if listaA[ren][col] == 0:
                listaA[ren][col] = ren + col
    return listaA



