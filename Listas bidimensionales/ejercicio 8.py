listas = [[1,-3,5,2,7,-3,8,3,-3,4], [-454,45,27,8,6,-35,12], [32,-535,-356,21,-64,7549]]


for lista in listas:
    x = [num * 0 if num < 0 else num for num in lista]
    print(x)

