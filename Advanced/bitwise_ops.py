#  (bin(19))
#  (int("0b10010",2))

'''
x=3
y=6
print(x&y)  #bitwise AND
print(x|y)  #bitwise OR
print(x^y)  #bitwise XOR
'''

'''
x=5  # left shift => multiply x with 2 to the power of y
print(x<<1)
print(x<<2)
print(x<<3)'
'''''
'''
x=5  # left shift => divide x with 2 to the power of y
print(x>>1)
print(x>>2)
print(x>>3) 
'''

'''
x=5
print(~x)
'''

def kthBit_set(n,k):
    if n & (1<<(k-1)):                 # alternate condition =>    (n>>(k-1)) & 1
        return True
    else: 
        return False

def naive_countSetBits(n):
    res = 0
    while n:
        if n%2==1:
            res += 1          # if statement can be optimised to res += (n&1)
        n = n//2
    return res
# Time comp = O(Number of bits)

def countSetBits(n):
    res = 0
    while n:
        n = n&(n-1)                #sets rightmost set bit to 0 in each iteration
        res += 1
    return res
#Time Comp = O(number of set bits)

def efficientCountSetBits(n):
    table = [0]*256

    for x in range(256):
        table[x] = (x&1) + table[x//2]
    
    return table[n&0xff] + table[(n>>8)&0xff]+ table[(n>>16)&0xff]+ table[(n>>24)&0xff]
#Time Comp = O(1)

def one_odd_occurring(l):
    x = 0
    for i in l:
        x = x ^i                 # x^0 = x, x^x = 0
    return 

def naive_power_of_two(n):
    i = 1
    while n>=i:
        if n==i:
            return True
        i = i<<1
    return False

def power_of_two(n):
    if n==0:
        return False
    return (n & (n-1) == 0)

def two_odd_occurring(l):
    xor = 0
    res1 = 0
    res2 = 0
    for i in l:
        xor = xor ^ i
    
    rightmost_setbit = xor & ~(xor-1)  #Finds the righmost set bit

    for i in l:
        if i & rightmost_setbit == 0:
            res1 = res1 ^ i
        else:
            res2 = res2 ^ i
    return (res1,res2)

def powerSet(s):
    n = len(s)
    pSize = 1<<n
    for i in range(pSize):
        for j in range(n):
            if i & (1<<j) != 0:
                print(s[j], end="")
        print()

def swapBits(self,n):
    #Your code here
    evenbit_mask = 0xAAAAAAAA
    oddbit_mask = 0x55555555
        
    evenbits = n&evenbit_mask
    oddbits = n&oddbit_mask
    evenbits = evenbits>>1
    oddbits = oddbits<<1
        
    return evenbits | oddbits

def countSetBitsTillN(n):
    if n<=0:
        return 0
    
    x = 0
    while (1<<x)<=n:
        x += 1
    x -= 1

    setBits_upto_pow2 = x*(1<<(x-1))
    msb_from_pow2_to_n = n - (1<<x) + 1
    remaining_bits = countSetBitsTillN(n - (1<<x))

    return setBits_upto_pow2 + msb_from_pow2_to_n + remaining_bits

def maxAND(l):
    max_and = 0
    for i in range(30,-1,-1):
        count = 0
        bit_mask = 1<<i
        candidate = max_and | bit_mask
        for x in l:
            if x & candidate == candidate:
                count += 1
            if count == 2:
                break
        if count==2:
            max_and = candidate
    return max_and

def binary_to_gray(n):
    return n ^ (n>>1)

def gray_to_binary(n):
    binary = 0
    while n:
        binary ^= n
        n>>1
    return binary

def own_grayToBinary(self,n):
    ##Your code here
    if n==0:
        return 0
    k = 0
    while (1<<k)<=n:
        k += 1
    k -= 1
    res = 1<<k
    for i in range(k-1,-1,-1):
        if n&(1<<i) != 0:
            if res & (1<<(i+1)) == 0:
                res = res | (1<<i)
        else:
            if res & (1<<(i+1)) != 0:
                res = res | (1<<i)
    return res


print(bin(23&0xff))