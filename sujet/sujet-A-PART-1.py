n = int(input('Entrer un entier naturel n'))
compteur = 0

for i in range(1, n+1):
  if n % i == 0:
    compteur +=1
    print(i)

if compteur == 2 :
  print("c'est un nombre premier")
else :
  print("Le nombre n'est pas premier ")
