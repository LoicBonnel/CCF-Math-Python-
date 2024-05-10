# Dm Bataille

from random import *
# A
paquet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

paquetA = []
paquetB = []

for k in range(49):
    i = randint(0, 9)
    j = randint(0, 9)
    temp = paquet[i]
    paquet[i] = paquet[j]
    paquet[j] = temp
print(paquet)

# B (deux sous paquets)

d = 0

while len(paquet) > d:
    carteEnCour = paquet[d]
    paquetA.append(carteEnCour)
    d = d + 2

d = 1

while len(paquet) > d:
    carteEnCour = paquet[d]
    paquetB.append(carteEnCour)
    d = d + 2
"""
# Egalise les paquets de cartes des joueurs A et B :

if len(paquetA) > len(paquetB):
    carte_en_trop = len(paquetA)
    paquetA.pop()         # pop --> supprime le derniere element d'une liste
"""


print("Carte pioché :", paquet)
print("Carte du joueur numéro A :", paquetA)
print("Carte du joueur numéro B :", paquetB)

# C

CompteurJA = 0
CompteurJB = 0

for d in range(len(paquetA)):
    print("Joueur A :", paquetA[d], "    Joueur B :", paquetB[d])
    carteJ1 = 0
    carteJ2 = 0

    if paquetA[d] > paquetB[d]:
        CompteurJA = CompteurJA + 1
    else:
        CompteurJB = CompteurJB + 1

print("Compteur Joueur A :", CompteurJA, "      Compteur Joueur B :", CompteurJB)

if paquetA > paquetB:
    print("Le joueur A à gagné la partie")
else:
    print("Le joueur B à gagné la partie")
