"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre amb respectius numeros i lletras;-)
"""
for x in range(8, 0, -1):
    print(x, end="")
    for y in range(8):
        if (x + y) % 2 == 0:
            print("⬜️", end="")
        else:
            print("⬛️", end="")
    print()
print(" a", "b", "c", "d", "e", "f", "g", "h")
