    """
Andres Diaz de Leon Valdes
A01620020
"""
#Variables que se usan para la funciones
matriculas = ["A01620020", "L01620020", "A01620018", "L1620018", "A016283463"] #para la segunda función
palabras = ["brasil", "mexico", "islandia", "nigeria","angola", "grecia", "suecia", "belgica", "cuba", "Bolivia"]
letra = "b"
numero = 5


#Funciones
def mayor_Ingresado():
    print("Ingrese un numero cualquier numero positivo")
    print("Si ingresa un numero negativo el programa da el numero mas grande dado ")
    t = True
    m = 0
    while t == True:
        n = float(input(">>"))
        if n > m:
            m = n
        if n < 0:
            break
    print(f"el numero mayor ingresado fue {m}")


def clasifica(matriculas):
    matriz = [[],[]]
    for linea in matriculas:
        if linea[0] == "A":
            matriz[0].append(linea)
        elif linea[0] == "L":
            matriz[1].append(linea)
    print(matriz)


def empiezan_Con(palabras, letra):
    cont = 0
    for elemento in palabras:
        if elemento[0].lower() == letra:
            print(elemento)
            cont += 1
    print(f"{cont} palabras en la lista incian con la letra {letra}")


def matriz_identidad(n):
    matriz = []
    for i in range(n):
        lista = []
        for j in range(n):
            if i == j:
                lista.append(1)
            else:
                lista.append(0)
        matriz.append(lista)
    print(matriz)

def calcula_promedio():
    archivo = open("final_laboratorio_G1.txt", "w")
    archivo.close()
    matriz = []
    try:
        arch = open("practicasG1.csv", "r")
    except:
        print("No se pudo abrir el archivo")
    else:
        for linea in arch:
            lista = (linea.strip().rstrip(",").split(","))
            matriz.append(lista)
        arch.close()
    try:
        archivo = open("final_laboratorio_G1.txt", "a")
    except:
        print("No se pudo crear el archivo")
    else:
        n = 1
        for lista in range(43):
            m = 1
            suma = 0
            for x in range(9):
                suma += int(matriz[n][m])
                m += 1
            promedio = suma/9
            n += 1
            print(promedio)
            archivo.write(matriz[n-1][0])
            archivo.write("\t")
            archivo.write(str(promedio))
            archivo.write("\n")



