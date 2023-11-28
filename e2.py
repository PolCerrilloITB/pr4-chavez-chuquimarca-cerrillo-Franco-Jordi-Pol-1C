"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""
altura = int(input("Altura del triangle: "))
if altura <= 9 and altura >= 2:
    for n in range(1, altura + 1):
        print(n, end=" ")
        for j in range(1, n-1):
            if n == altura:
                print(n, end=" ")
            else:
                print(" ", end=" ")
        print(n)