"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
30/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes
"""
#Primero definimos las variables que vamos a "multiplicar", el contador que aumenta y una variable de apoyo.
x = int(input())
y = int(input())
sumaT = x
apoyo = 0
#Sumamos a una variable misma el numero de veces que es la otra variable
for n in range(1, y+1):
    sumaT = sumaT + x * apoyo
    if apoyo == 0:
        apoyo += 1
print(sumaT)
