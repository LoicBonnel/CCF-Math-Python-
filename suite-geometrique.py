# Définition : suite géométrique, programme qui calcule le rang d'une suite géométrique
# saisie par l'utilisateur

Un1 = 1
Un2 = 1

rang = int(input("Veuillez saisir le rang, le programme vous donnera le résultat"))

rang = rang - 1

resultat = 0
n = 0

while n < rang:
    resultat = Un1 + Un2
    Un2 = Un1
    Un1 = resultat
    n = n + 1

print(resultat)
