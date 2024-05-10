N = int(input("veuillez saisir une valeur"))
print("N est de ",N)
while N > 1 :
  DIV = 2
  while N % DIV != 0:
    DIV += 1
  N = N//DIV
  print(DIV)
