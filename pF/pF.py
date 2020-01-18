def apertura_archivo_Poblacion():
    try:
        arch=open("Poblacionporsexo_rangoedad.csv","r",encoding="UTF-8",errors="ignore")
    except IOError:
        print("No se puede abrir el archivo o no existe.")
    else:
        matriz = []
        arch.readline()
        for linea in arch:
            lista = (linea.rstrip().rstrip(",").split(","))
            matriz.append(lista)
        arch.close()
        return matriz

print(apertura_archivo_Poblacion())