"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que imprimeix un tauler d’escacs per pantalla.
Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
"""

for x in range(8):
   for y in range(8):
       if (x + y) % 2== 0:
           print("⬜️", end="")
       else:
           print ("⬛️", end="")
   print ()

   h