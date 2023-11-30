"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre amb respectius numeros i lletras;-)
"""
# Posar els numeros a las columnes d'aball amunt i que es repetixi x vegades
for x in range(8, 0, -1):
    print(x, end="")
    # Posar que es repetixi y vegades i printi les quadricules adequades
    for y in range(8):
        if (x + y) % 2 == 0:
            print("⬜️", end="")
        else:
            print("⬛️", end="")
    print()
    # Printar las lletras de las filas
print(" a", "b", "c", "d", "e", "f", "g", "h")
