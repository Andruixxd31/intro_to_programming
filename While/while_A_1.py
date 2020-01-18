num = 0
print("Ingrese el número de incio (entero positivo)")

inicio = input(">>")
if not inicio.isdigit():
    while not inicio.isdigit():
        print("Entrada no valida")
        inicio = input(">>")
print("Ingrese el ultimo numero del rango")

fin = input(">>")
finInt = int(fin)
inicioInt = int(inicio)
if not fin.isdigit() or finInt < inicioInt:
    while not fin.isdigit() or finInt < inicioInt:
        print("Entrada no valida, verifique el valor")
        fin = input(">>")
        finInt = int(fin)

inicio = int(inicio)
fin = int(fin)
while inicio <= fin:
    print(inicio)
    inicio += 2