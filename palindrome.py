# Définition palindrome  -->  mot ou phrase se lisant dans les 2 sens exemple : KAYAK

phrase = "kayak"
envers = ""
p = 0

while p < len(phrase):               #tant que p est inférieur à la taille de phrase
    envers = (phrase[p]) + envers    # envers prend la lettre numéro p de phrase
    p += 1                           # on incrémente la boucle p

if phrase == envers:
    print(phrase, "est un palindrome")
else:
    print(phrase, "n'est pas un palindrome")
