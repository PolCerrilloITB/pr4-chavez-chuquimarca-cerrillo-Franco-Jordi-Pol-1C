"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que mostra per pantalla la suma de tots els nombres senars i
de tots els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
( Ex: si el límit és 31 sumaParells 240 i sumaSenars 225)
"""
# Variables establertes i contadors
limite = int(input())
sPares = 0
sImpares = 0
# Condició perque es repeteixi el cop de vegades fins arribar a (limite)
for n in range(1, limite):
    # Condició per sumer els resultats al parells o impars
    if n % 2 == 0:
         sPares += n
    else:
         sImpares += n
print(sPares)
print(sImpares)