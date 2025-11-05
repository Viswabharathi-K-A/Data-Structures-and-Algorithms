import math

#n = int(input("Enter the number "))

def count_digit(n):
    dig = 0
    while n>0:
        n = n//10
        dig += 1
    return dig
#TimeComp = Theta(d); AuxSpace = O(1) (d = number of digits)


def palindrome_alt(n):
    x = n
    ld = 0
    while(x>0):
        uni = x%10
        ld = ld*10 + uni
        x = x//10
    if(ld==n):
        return True
    else:
        return False
#TimeComp = Theta(d); AuxSpace = O(1) (d = number of digits)

    
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#TimeComp = O(n); AuxSpace = O(n) 
    

def euclidean(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a
#TimeComp = O(min(a,b)); AuxSpace = O(1)

def extended_euclidean(a,b):
    if b == 0:
        return a

    else:
        return extended_euclidean(b, a%b)
#TimeComp = O(logmin(a,b)); AuxSpace = O(logmin(a,b))

def lcm_efficient(a,b):
    gcf = extended_euclidean(a,b)
    return (a*b)//gcf


def isprime(n):
    if n == 1:
        return "Neither prime nor composite"
    i = 2
    while i*i<n:
        if n%i == 0:
            return False
        i += 1
    return True
#TimeComp = O(sqrt(n)); AuxSpace = O(1)

def efficient_prime(n):
    if n == 1:
        return "Neither prime nor composite"
    if n == 2 or n == 3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i += 6
    return True
#TimeComp = O(sqrt(n)); AuxSpace = O(1)

def naive_prime_factorisation(n):
    
    for x in range(2,n+1,1):
        if efficient_prime(x):
            while n%x ==0:
                print(x, end=" ")
                n //= x

def unsorted_divisors(n):
    i = 1
    while i*i<=n:
        if n%i==0:
            print(i)
            if i!=n/i:
                print(int(n/i))
        i += 1
#TimeComp = O(sqrt(n)); AuxSpace = O(1)

def sorted_divisors(n):
    i = 1
    while i*i<n:
        if n%i==0:
            print(i, end =" ")
        i += 1
    while i>=1:
        if n%i==0:
            print(int(n/i), end = " ")
        i -= 1
#TimeComp = O(sqrt(n)); AuxSpace = O(1)

def sieve_of_eratosthenes(n):
    if n<=1:
        return
    isPrime = [True]*(n+1)
    i=2
    while i*i<=n:
        if isPrime[i]:
            for x in range(2*i,n+1,i):
                isPrime[x] = False
        i += 1
    for y in range(2,n+1):
        if isPrime[y] == True:
            print(y, end = " ")

def efficient_sieve(n):
    if n<= 1:
        return
    i = 2
    isPrime = [True]*(n+1)
    while i<=n:
        if isPrime[i]:
            print(i, end=" ")
            for x in range(i*i,n+1,i):
                isPrime[x] = False
        i += 1
#TimeComp = O(n*log(log(n))); AuxSpace = O(n)

def trailingZeroes_in_factorial(n):
    i = 5
    count = 0
    while i<=n:
        count += (n//i)
        i *= 5
    return count
#Time Complexity O(log₅(x)), Auxillary Space = O(1)


def efficient_compute_power(x,n):
    if n==0:
        return 1
    temp = efficient_compute_power(x,n//2)
    temp = temp*temp
    if n%2 == 0:
        return temp
    else:
        return temp * x
#time comp = O(log₂n), space comp = O(log₂n)

def binary_exponentiation(x,n):
    if n == 0:
        return 1
    res = 1
    while n>0:
        if n%2!=0:
            res = res*x
        x = x*x
        n = n//2
    return res
#time comp = O(log₂n), space comp = O(1)


print(efficient_compute_power(9,9))