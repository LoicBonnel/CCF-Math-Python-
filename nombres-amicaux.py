def sdiv(n):
    s = 0
    for i in range (1, n):
        if n % i == 0 :
            s = s + i
    return s

print(sdiv(220))
print(sdiv(284))


def ami (n, p):
   for i in range(1, n+1):
        for j in range(i+1, p+1):
            if  sdiv(n) == j and  sdiv(j) ==  n :
                print(i,j)

print(ami(1500, 1500))
