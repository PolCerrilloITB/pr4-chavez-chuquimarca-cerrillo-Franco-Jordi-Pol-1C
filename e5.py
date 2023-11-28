"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que demana a l'usuari la introducció de 10 nombres sencers i ha de mostrar,
al final i per pantalla, quants són positius, quants negatius i quants zero.
"""
x = int(input())
y = int(input())
sumaT = x
apoyo = 0
for e in range(1, y+1):
    sumaT = sumaT + x * apoyo
    if apoyo == 0:
        apoyo += 1
print(sumaT)