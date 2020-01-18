"""
Andrés Díaz de León
A01620020
Programa que hace conversiones de los galones de gasolina indicados
"""

print("Ingrese la cantidad de galones de gasolina que compro")
gasGalones = float(input(">>"))
gasLitros = gasGalones*3.78541
barilPe = gasGalones/19.5
barilGas = gasGalones/42.5
C02 = barilGas*20

print("galones de gasolina: %5.2f" % (gasGalones))
print("Litro de gasolina: %5.2f" % (gasLitros))
print("Barilles necesarios para tener esa cantidad de gas: %5.2f" % (barilPe))
print("CO2 producido %5.2f" % (C02))