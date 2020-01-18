"""
Andrés Díaz de Leon
A01620020
"""
def lee_archivo():
    matriz = []
    try:
        archivo=open("calif.txt")
    except IOError:
        print("No se puede abrir ó no se encuentra el archivo")
    else:
        for linea in archivo:
            lista = (linea.rstrip().split(" "))
            print(lista)
            matriz.append(lista)
    print(matriz)
    return matriz



def calif_final(matriz):
    for alumno in matriz:
        print(alumno)
        primer_parcial = int(alumno[1]) * 0.25
        segundo_parcial = int(alumno[2]) * 0.45
        proyecto = int(alumno[3]) * 0.30
        promedio = (primer_parcial + segundo_parcial + proyecto)
        alumno.append(round(promedio))
        try:
            arch = open("Calificaciones.txt", "w+")
        except:
            print("No se puede abrir ó no se encuentra el archivo")
        else:
            for linea in matriz:
                print(linea)
                arch.write(str(linea))
    print(matriz)
    return matriz

def promedio_parcial(matriz):
    primer_parcial = 0
    segundo_parcial = 0
    final = 0
    lista =[]
    for alumno in matriz:
        primer_parcial = primer_parcial + int(alumno[1])
        segundo_parcial = segundo_parcial + int(alumno[2])
        final = final + int(alumno[4])
    lista.append((primer_parcial / len(matriz)))
    lista.append((segundo_parcial / len(matriz)))
    lista.append((final / len(matriz)))
    return lista

def despliega_finales(matriz):
    lista1 = []
    for alumnos in matriz:
        alumnos[0] = int(alumnos[0])
        alumnos[-1] = int(alumnos[-1])
        lista1.append([alumnos[0], alumnos[-1]])
    return lista1

matriz = lee_archivo()
calif_final(matriz)

