def codeacces(id):          # On crée notre fonction code d'accès
    p=id; s=0; k=1

    while k <=4 :           # tant que k est inférieur ou égale à 5
        u = p % 10
        k = k + 1
        s = s + k * u
        p = (p - u) // 10
    r = s % 7
    cle = 7 - r
    return print("votre identifiant est", cle)  # On retourne la valeur de cle en console

#id = input("Veuillez saisir l'identifiant")
codeacces(3732)
