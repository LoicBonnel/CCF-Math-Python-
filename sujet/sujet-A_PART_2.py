a = int(input("Entrer deux entier strictement positifs"))
b = int(input("Entrer deux entier strictement positifs"))

while b != 0 :
  a, b = b, a % b
print(a)

