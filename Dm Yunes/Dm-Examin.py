#Dm Mr Yunes Examin

# A1 création des variables

matieres = ["Francais", "Mathématiques", "Histoire-Géographie", "LV1", "LV2", "Physique", "Technologie"]
coefMatiere = [3, 3, 2, 2, 1, 2, 1, 2]
note = []
moyenne = 0
noteEnCour = 0
totalCoef = 0
points_gagnes = 0

noteOption = float(input("Veuillez saisir la note option :"))

if noteOption < 10:
    points_gagnes = 0
else:
   points_gagnes = (noteOption - 10)*2
   moyenne = points_gagnes

print("Point gagné par votre option :", points_gagnes)

# A2 Saisie des notes

for j in range(len(matieres)):
    print("Veuillez saisir votre note de : ")
    noteEnCour = (float(input(matieres[j])))
    note.append(noteEnCour)

# A3 Calcule moyenne

for i in range(len(note)):
    moyenne = moyenne + (note[i] * coefMatiere[i])
    totalCoef = totalCoef + coefMatiere[i]

moyenne = moyenne / totalCoef

print("Voici vos notes saisies :", note)
print("La moyenne est de", moyenne)

# A4 Candidat reçus ou non + mention

if moyenne >= 16 :
    print("reçus, mention très bien")
elif moyenne >= 14 :
    print("reçus, mention bien")
elif moyenne >= 12 :
    print("reçus, mention assez bien")
elif moyenne >= 10 :
    print("reçus, mention passable")
elif moyenne < 10 :
    print("Vous n'êtes pas reçus")
