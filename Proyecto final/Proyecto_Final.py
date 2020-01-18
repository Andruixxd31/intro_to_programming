import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
import time, sys


def porcentaje_madres_adolescentes(municipio,anio):
    matriz = apertura_archivo_madres()
    for lista in matriz:
        listaAnios = [2010,1,2011,7,2012,13,2013,19,2014,25,2015,31,2016,37,2017,43] #Lista que contiene los años y sus valores a usar
        if anio in listaAnios:
            m = listaAnios[listaAnios.index(anio) + 1] #Se obtiene el valor a lado del año especificado
        if lista[0].lower() == municipio: #Los municipios se convierten a minisculas por eso lista[0] también lo es para poder comparar
                nacimientos = (int(lista[m+1])+int(lista[m+2]))/int(lista[m])*100
                print(lista[m+1])
                print(lista[m+2])
    print(f"El {nacimientos: 2.2f}% de las madres en el año {anio} son de mujeres menores a de 19 años")
    return


def menor_madres_adolescentes(municipio):
    matriz = apertura_archivo_madres()
    aniosMenorNacimientos=[] #Matriz que contendra el año y el numero de mandres
    for lista in matriz:
        if lista[0].lower() == municipio:
            n=2
            m=3
            b = int(lista[1])
            for x in range(7): #Loop para recorrer las 7 años disponibles en el csv.
                a = int(lista[n]) + int(lista[m])
                print(a)
                if a < b:
                    b = a
                    aniosMenorNacimientos.clear()



                    
                    aniosMenorNacimientos.append(matriz[0][n-1])
                    aniosMenorNacimientos.append(a)
                elif a == b:
                    aniosMenorNacimientos.append(matriz[0][n-1])
                    aniosMenorNacimientos.append(a)
                n += 6
                m += 6
    print(aniosMenorNacimientos)
    return


def porcentaje_madres_15():
    arch = open("madres_menores15_2015.txt", "w")
    arch.write("Porcentaje de madres menores de 15 en el 2015 an cada municipio\n\n")
    arch.close() #crea el titulo del archivo
    matriz_madres = apertura_archivo_madres()
    matriz_pob = apertura_archivo_poblacion()
    n = 1
    for x in range(125):
        N = 3
        for x in range(124):
            if matriz_madres[n][0] == matriz_pob[N][0]:
                municipio = matriz_madres[n][0]
                porcentaje = "{0:.5f}".format(int(matriz_madres[n][32])/int(matriz_pob[N][4])*100)
                porcentaje = str(porcentaje)
                try:
                    arch = open("madres_menores15_2015.txt", "a") #Agrega la info de cada municipio
                except:
                    print("No se pudo abrir el archivo")
                else:
                    arch.write(f"{municipio}\t {porcentaje}% \n")
            N += 1
        n += 1
    print("Su archivo se acaba de generar")

"""
No todos los municipios tiene la info de su poblacion o del numero de madres 
Ademas los municipios en el documento de población no estan totalmente ordenados por orden alfabeticp
Por ello el problema 3 tiene que estar viendo cada lista anidada de la matriz_pob para ver si 
el municipo esta presente en ambos documentos
"""


def municipio_mayor_madres_15(anio):
    matriz = apertura_archivo_madres()
    b = 0
    n = 1
    numerosMayores = []
    listaAnios = [2010,2,2011,8,2012,14,2013,20,2014,26,2015,32,2016,38,2017,44]
    m = listaAnios[listaAnios.index(anio)+1]
    for x in range(125):
        a = int(matriz[n][m])
        if a > b: #Se crea una lista para agregar a los municipios con mayor numero de nacimientos
            b = a
            numerosMayores.clear()
            numerosMayores.append(matriz[n][0])
            numerosMayores.append(a)
        elif a == b:
            numerosMayores.append(matriz[n][0])
            numerosMayores.append(a)
        n += 1
    return(numerosMayores)

"""
def grafica():
    y = []
    m = 2
    matriz = apertura_archivo_madres()
    for i in range(8):
        n = 1
        b = 0
        for j in range(125):
            a = int(matriz[n][m])
            if a > b or a == b:  # Se crea una lista para agregar a los municipios con mayor numero de nacimientos
                b = a
                y.clear()
                print(a)
                y.append(a)
            n += 1
        print(y)
        m += 6
        print(m, "m")
    print(y)
"""


def municipio_menor_madres_15(anio):
    matriz = apertura_archivo_madres()
    b = 0
    n = 1
    numerosMenores = []
    listaAnios = [2010, 2, 2011, 8, 2012, 14, 2013, 20, 2014, 26, 2015, 32, 2016, 38, 2017, 44]
    m = listaAnios[listaAnios.index(anio) + 1] #manera de designar m que se sa para ver columnas
    for x in range(125):
        a = int(matriz[n][m])
        if a < b:  #Se crea una lista para agregar a los municipios con menor numero de nacimientos
            b = a
            numerosMenores.clear()
            #si se encuentra un municipio con menos nacimientos que antes visto elimina lo puesto dentro de la lista
            numerosMenores.append(matriz[n][0])
            numerosMenores.append(a)
        elif a == b:
            numerosMenores.append(matriz[n][0])
            numerosMenores.append(a)
        n += 1
    return (numerosMenores)

"""
Validaciones, modificaciones de variables y apertura de los archivos
"""

def validacion_string(): #Hace que el string no pueda ser mal puesto
    string = input("Ingresa un municipio: ")
    string = string.lower().rstrip().lstrip()
    return string

def validacion_numero(numero): #valida que se meta un entero
    while True:
        try:
            int(numero)
            numero = int(numero)
            break
        except ValueError:
            print("Entrada no valida.")
            numero = input('Nueva entrada: ')
    return numero

def apertura_archivo_madres(): #Crea una matriz bidimensional del archivo
    try:
        archivo = open("Nacimientos1.csv", "r")
    except:
        print("No se puede abrir el archivo.")
    else:
        matriz = []
        for linea in archivo:
            lista = (linea.rstrip().rstrip(",").split(","))
            matriz.append(lista)
    archivo.close()
    return matriz

def apertura_archivo_poblacion(): #Crea una matriz bidimensional del archivo
    try:
        archivo=open("Poblacion_2015.csv", "r")
    except:
        print("No se puede abrir el archivo.")
    else:
        matriz=[]
        for linea in archivo:
            if "Total" in linea: #Elimina el numero que viene a lado de cada municipio en "pobalacion_2015"
                lista = (linea.strip().rstrip(",").split(","))
                clean = lista[0]
                print(lista[0])
                clean = clean[4:]
                lista.remove(lista[0])
                lista.insert(0,clean)
                matriz.append(lista)
    archivo.close()
    return matriz

#Menu y opciones



def opciones():
    op = input(">>")
    op = validacion_numero(op)
    if op == 1:
        municipio = validacion_string()
        anio = (input("Ingresa un año: "))
        anio = validacion_numero(anio)
        porcentaje_madres_adolescentes(municipio, anio)
    elif op == 2:
        municipio = validacion_string()
        menor_madres_adolescentes(municipio)
    elif op == 3:
        porcentaje_madres_15()
    elif op == 4:
        anio = (input("Ingresa un año: "))
        anio = validacion_numero(anio)
        lugar = municipio_mayor_madres_15(anio)
        print(lugar)
    elif op == 5:
        anio = (input("Ingresa un año: "))
        anio = validacion_numero(anio)
        lugar = municipio_menor_madres_15(anio)
        print(lugar)
    elif op == 6:
        quit()
    else:
        print("número no valido")

while True: #Loop infinito. Solo la opción 6 termina el programa
    print("\u001b[31;1mOpciones \nIngrese un número porfavor")
    print("\u001b[31;1m\u001b[31;1m[1]\t\t Porcentajes de madres adolescentes ")
    print("[2]\t\t Año con menor número madres adolescentes")
    print("[3]\t\t Porcentaje de madres menores de 15 en el 2015")
    print("[4]\t\t Municipio con mayor numero de madres menores de 15 años")
    print("[5]\t\t Municipio con menor número de madres menores de 15 años")
    print("[6]\t\t Salir\u001b[0m" )
    opciones()
