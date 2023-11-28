"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que mostra per pantalla la suma de tots els nombres senars i
de tots els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
( Ex: si el límit és 31 sumaParells 240 i sumaSenars 225)
"""
limite = int(input())
nPares = 0
nImpares = 0
l = 1
sPares = 0
sImpares = 0
sP = 1
sI = 1
for limite in range(1,limite+1):
    if l%2 == 0:
         nPares += 1
    elif l%2 != 0:
         nImpares += 1
    l += 1
for nPares in range(1, nPares+1, 2):
    sPares = sPares + sP
    sP += 2
for nImpares in range(1, nImpares+1, 2):
    sImpares = sImpares + sI
    sI += 2
print(sImpares)