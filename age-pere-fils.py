ageFils = int(input("Entrer l'age du fils : "))     # On demande l'âge du fils en console
agePere = int(input("Entrer l'age du père : "))     # On demande l'âge du père en console
annee = 0            # On initialise la variable annee à 0

while (agePere/2) != ageFils :  # Tant que l'âge du père / 2 n'est pas égale à l'âge du fils
    ageFils += 1                # ageFils = ageFils + 1
    agePere += 1                # agepere = agepere + 1
    annee += 1                  # annee = annee + 1

print("La différence est de ", annee, " ans")
print("L'age du fils est de ", ageFils, " ans")
print("L'age du pere est de ", agePere, " ans")
