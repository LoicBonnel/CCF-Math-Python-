# Définition addition chiffre  -->  Programme qui additionne les chiffres d'un nombre

# exemple : 256 --> 2 + 5 + 6 --> 13

def additionChiffre(n):     # Ont créer la fonction additionChiffre
    s = 0                   # Initialisation de S à 0
    while n > 0:            # tant que n est suppérieur à 0
        s = s + n % 10
        n = n // 10
    return s                # On retourne la valeur de S en console

n = int(input("Entrer un nombre, le programme additionnera tous ces chiffres")) # on demande la valeur en console
print(additionChiffre(n)) # on affiche le resultat de la fonction addition chiffre


