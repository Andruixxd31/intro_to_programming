"""
Andrés Díaz de León
A01620020
Viendo la categoria de un huracan con su velocidad en km
"""
print("ingrese la velocidad del huracan, (en kmh)")
velocidadKm = float(input(">>"))
velocidadM = velocidadKm/1.6
print(f"Equivalent a {velocidadM} millas")


if velocidadM < 75:   #Mide las categorias con millas si es menor a 75 no hay huracan
    print("No es un huracan")
elif velocidadM >=75 and velocidadM < 96:
    print("""Categoria      Daños
    1         Minimos""")
elif velocidadM >=96 and velocidadM < 111:
    print("""Categoria      Daños
    2         Moderados""")
elif velocidadM >= 111 and velocidadM < 130:
    print("""Categoria      Daños
    3         Extremos""")
else:
    print("""Categoria      Daños
     4       Catastróficos""")