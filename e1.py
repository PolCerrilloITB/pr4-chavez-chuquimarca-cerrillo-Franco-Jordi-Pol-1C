"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
28/11/2023
ASIXc1C M03 UF1
Descripcion: Programa que demana a l'usuari la introducció de 10 nombres sencers i ha de mostrar,
al final i per pantalla, quants són positius, quants negatius i quants zero.
"""
# Contadors de positiu, negatiu, i zeros.
contPos = 0
contNeg = 0
contZer = 0
# Repetició de 10 cops
for i in range(10):
 nSencers = int(input("Donam 1 numero sencer: "))
# Regles de positius negatius i zeros
 if nSencers > 0:
  contPos = contPos + 1
 elif nSencers < 0:
  contNeg = contNeg + 1
 else:
  contZer = contZer +1
print("Positius:", contPos, "Negatius:", contNeg, "Zeros:", contZer)