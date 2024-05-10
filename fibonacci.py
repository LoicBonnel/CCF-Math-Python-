# Fibonacci

def FIBONACCI(n):
    if n == 0  or n == 1 :
        return n
    else:
        return(FIBONACCI(n-1) + FIBONACCI(n-2))

n = int(input("Saisire le rang"))
print ('FIBONACCI de rang',n,'=',FIBONACCI(n+1))
