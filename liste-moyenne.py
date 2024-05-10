#list
nbrnote = int(input("nb de note ?"))         # On demande le nombre de note en console
list = []                                        # On crée une list [list]
for k in range(nbrnote):                      # for k in nbrnote
    list.append(int(input("donner une note")))      # la list prend la valeur saisir en console

#moyenne
moyenne = 0
nbrMax = 0
nbrMin = 20

for k in range(len(list)):          # for k in longeur liste
    moyenne = list[k] + moyenne

    if list[k] > nbrMax:            # si la valeur en liste [k] est > nbrmax il prend sa valeur
        nbrMax = list[k]

    if list[k] < nbrMin:              # si la valeur en liste [k] est < nbrmax il prend sa valeur
        nbrMin = list[k]

    k = k + 1                   # on incrémente la boucle k

moyenne = moyenne/len(list)     # la moyenne est égale à la moyenne divisé par la longeur de la liste

nbr = 0

for k in range(len(list)):           # for k in longeur liste
    if list[k] > moyenne :           # on vérifie si la note est au dessus de la moyenne
        nbr+=1                       # On incrémente nbr
    k +=1                            # On incrémente K


print ("La moyenne des notes est ",moyenne)
print ("la note maximale est ",nbrMax)
print ("la note minimal est ",nbrMin)
print ("le nombre de notes superieur a la moyenne est de :",nbr)
