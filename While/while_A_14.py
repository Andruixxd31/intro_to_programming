"""
Programa que trabaja con 2 vectores  para obetener diferentes resultados
Andrés Díaz de León
A01620020
"""
print("Introduzca los puntos del primer vector")
print("Vector 1: ")
x1 = float(input("X: "))
y1 = float(input("Y: "))
z1 = float(input("Z: "))
print("Introduzca los puntos del segundo vector")
x2 = float(input("X: "))
y2 = float(input("Y: "))
z2 = float(input("Z: "))

print(f"Vector 1 ({x1}, {y1}, {z1}) // Vector 2 ({x2}, {y2}, {z2})")

resp = 0
while resp != 5:
    print("""
          [1] Suma vectorial
          [2] Diferencia de los vectores 
          [3] Producto escalar
          [4] Producto vectorial
          [5] Salir
          [cualquier otro numero] dibujo""")

    def suma():
        x = x1 + x2
        y = y1 + y2
        z = z1 + z2
        print(f"La suma nos da el vector ({x}, {y}, {z})")

    def diferencia():
        x = x1 - x2
        y = y1 - y2
        z = z1 - z2
        print(f"La diferencia nos da el vector ({x}, {y}, {z})")

    def productoEscalar():
        x = x1*x2
        y = y1*y2
        z = z1*z2
        print(f"El producto escalar nos da el vector ({x}, {y}, {z})")

    def productoVectorial():
        x = y1*z2 - y2*z1
        y = z1*x2 - z2*x1
        z = x1*y2 - x2*y1
        print(f"El producto vectorial nos da el vector ({x}, {y}, {z})")

    def dibujo():
        print("""
      ,-'   >---.        ,---.
     /  ,o)'     `.     /     `.
    '|    (   ,_   )   |        `.
  ,--|    -.,'  `./    ;        `.
 /   |      `.         :   .      `
/    |:.      `-       ,    \    :.|
|   ,-|'        \-.___,'     :\   ;::|
|, ::'\   ,      `.        ,.::\   :(-
|: |:; \,'\  ).   / .:..  ,:::::\   `|
|  |,:  `  `/  `-/ ::::::::::::::\    ;
|   |:             ::::::::::::::.\   |
\   |:.,           ::::::::::   ` |;  |
\  `.:'       ::.,::::::: `:  \  ||  |
 \   \     . ,:::::::,:::  . ( `-'|  |
  `.  \     ::::,`':(::' ` |\ \   :  |
    \  :-:. `::      \ `   | \ \   \ |
     `'  |:' `'  /`.  `. \ :  `'    \|
        /   \    \ `._/ `'`-`        |
    __ / \, ,\   _|  `.
  _/ ,\- (`'  `-',-','-,"-.
 /,-(,- \_\     (-'(,---.:.)
 `   `    '      `  `    '
        """)

    resp = int(input(">> "))
    if resp == 1:
        suma()
    elif resp == 2:
        diferencia()
    elif resp == 3:
        productoEscalar()
    elif resp == 4:
        productoVectorial()
    elif resp == 5:
        print("Adios")
    else:
        dibujo()

#Practique el uso de funciones