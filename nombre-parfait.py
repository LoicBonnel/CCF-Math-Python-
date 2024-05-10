# Définition : Les nombres parfaits sont des entiers égaux à la somme de leurs diviseurs.
# Exemple : 6 se divise par 2, 3 et 1. En additionnant 2, 3 et 1, on arrive à 6 !
# Même chose pour 28, somme de 1 + 2 + 4 + 7 + 14.

def nbrParfait(n):          # On crée notre fonction nbrParfait
    s = 0                   # On initialise la variable s = 0

    for i in range ( 1 , n ):     # On créer la boucle for i ion range en l'ocurence de 1 à n
        if n % i == 0:            # Si n % i = = 0 alors
            s = s + i
    if s == n :                                     # if s == n alors (nbr parfait)
        print (n, "est un nombre parfait")
    else :                                          # sinon alors (nbr pas parfait)
        print (n, "n'est pas un nombre parfait")

nbrParfait(int(input("Veuillez saisir un nombre entier, vous serez si il est parfait ou pas")))
