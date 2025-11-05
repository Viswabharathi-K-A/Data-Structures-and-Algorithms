def oneToN(n):
    if n==0:
        return
    oneToN(n-1)
    print(n)


def NToOne(n):
    if n==0:
        return
    print(n)
    NToOne(n-1)

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fibonacci(n-1)+fibonacci(n-2)

def sum_of_digits(n):
    if n//10==0:
        return n
    return n%10 + sum_of_digits(n//10)

def checkPalin(self, N, st, end):
    if st >= end:
        return True
    return N[st] == N[end] and checkPalin(N, st+1, end-1)
#TimeComp = O(n) SpaceComp = O(n)

    

