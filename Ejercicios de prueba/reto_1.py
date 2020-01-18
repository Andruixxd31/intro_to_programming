"""
Recibir una lista con 0's, 1's y 2's acomodados al azar.
Regresar una lista con los valores acomdodados por orden.
- No se pueden usar funciones
0: 6
1: 5
2: 9

Otro ejercicio: En uns lista ordenada encontrar la posición de un elemento
"""

miLista = [0,2,2,0,1,2,2,1,2,0,0,2,2,1,1,0,2,1,0,2]

"""
for x in range(3):
    for num in range(len(miLista)):
        print(miLista[num])
        if miLista[num] == x:
            miOtraLista.append(miLista[num])

print(miOtraLista)
"""

for x in range(len(miLista)):
    if miLista[x] == 0:


    elif miLista[x] == 2:
        a = miLista[len(miLista)-1]
        b = miLista[x]
        miLista[x] = a
        miLista[len(miLista)-1] = b



print(miLista)


