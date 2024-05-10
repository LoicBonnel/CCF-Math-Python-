# Définition : programme qui calcule le nombre de fois que la lettre "X" apparait dans une
# phrase saisie par l'utilisateur

lettre = input(str("Veuillez saisir une lettre, le programme vous dira le nombre de fois qu'elle apparait dans votre phrase"))

lettre = lettre.lower()             # on met la lettre en minusucle

phrase = input("Veuillez saisir une phrase, le programme calculera le nombre de fois que la lettre est saisie :")

longeurPhrase = len(phrase)

print("La longeur de la phrase  est de", longeurPhrase)

nbrCarac = 0

for k in range(0, longeurPhrase):   # boucle for de k à longeur phrase
    if(phrase[k]) == lettre:        # si
        nbrCarac +=1                # on incrémente nbrCarac

print("Le nombre de lettre",lettre,"est de ", nbrCarac)
