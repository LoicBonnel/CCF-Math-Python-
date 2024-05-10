# Définition factorielle, exemple pour 5 --> 5 * 4 * 3 * 2 * 1 --> 120

n = int(input("Donnez le nombre n :"))   # On demande de saisir le nombre n en console
m = 1                                   # On initialise la variable m = 1
for i in range(1, n+1) :                # On crée une boucle for i in range en l'occurence de 1 à n
    m *= i                              # m =  m * i
print(m);                               # on affiche la valeur de m en console
