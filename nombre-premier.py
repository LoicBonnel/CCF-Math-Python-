# Définition nombre premier : nombre qui se divise par lui même et 1 (sachez que 2 est le seul nombre premier paire)

#liste nombre premier = [1,2,3,5,7,11,13,17,19,23 ...]

#  Le programme recense les diviseurs de nombre premier -->  18 = 2 * 3 * 3

# par exemple pour 18 --> 18 / 2 = 9
# 9 / 3 = 3
# 3 / 3 = 1


n = int(input("Veuillez saisir N : "))
print("N est de", n)
while n > 1 :
    Div = 2
    while n % Div != 0:
        Div = Div + 1  # quand le reste est différents de 0 div = div + 1 --> principe de division euclédienn
    n = n / Div
    print(Div)
def factor(n) :
    L = []
    Div = 2
    while n > 1 :
        if n % Div == 0:
            L.append(Div)
            n = n / Div
        else :
            Div = Div + 1
    return L
print(factor(18))
