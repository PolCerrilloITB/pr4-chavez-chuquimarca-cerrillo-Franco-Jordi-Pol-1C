"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes
"""
x = int(input())
y = int(input())
sumaT = x
apoyo = 0
for n in range(1, y+1):
    sumaT = sumaT + x * apoyo
    if apoyo == 0:
        apoyo += 1
print(sumaT)
