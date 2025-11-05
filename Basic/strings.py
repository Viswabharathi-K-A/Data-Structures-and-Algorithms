def reverse_string(s):
    rev = ""
    for i in s:
        rev = i + rev
    print(rev)

def check_rotation(s1, s2):
    if len(s1)!=len(s2):
        return False
    s3 = s1+s1
    print(s2 in s3)

def check_palindrome(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i=i+1
        j=j-1
    return True

def check_palindrome_short(s):
    return s==s[::-1]

def check_subsequence(s1,s2):
    i=0
    j=0  
    while i<len(s1) and j<len(s2):
        if s1[i]==s2[j]:
            j = j+1
        i=i+1
    return True if j==len(s2) else False

def recursive_check_subsequence(s1,s2,i,j):
    if j==len(s2):
        return True 
    if i==len(s1):
        return False
    if s1[i]==s2[j]:
        return recursive_check_subsequence(s1, s2, i+1, j+1)
    else:
        return recursive_check_subsequence(s1, s2, i+1, j)

def check_anagram(s1,s2):
    if len(s1)!= len(s2):
        return False
    count = [0]*256
    for x in range(len(s1)):
        count[ord(s1[x])] += 1
        count[ord(s2[x])] -= 1

    for x in count:
        if x!= 0:
            return False
    return True    

def naive_leftmost_repeating_char(s):
    for x in range(len(s)-1):
        for y in range(x+1,len(s)):
            if s[x]==s[y]:
                return x
    return -1
#Tine Comp = O(n*n), Space Comp = O(1)

def leftmost_repeating_char(s):
    d = dict()
    for x in s:
        if x in d.keys():
            d[x] += 1
        else:
            d[x] = 1
    temp = 1
    for x in s:                            #or use -> for x in d:
        if d[x] > temp:
            return s.index(x)
    return -1
#Tine Comp = O(n) - two traversals, Space Comp = O(1)

def efficient_leftmost_repeating_char(s):
    import sys
    count = [-1]*256                     #total unicode values
    res = sys.maxsize
    for i in range(len(s)):
        if count[ord(s[i])]==-1:
            count[ord(s[i])] = i
        else:
            res = min(res,count[ord(s[i])])
    if res == sys.maxsize:
        return -1
    else:
        return res
#Tine Comp = O(n) - one traversal, Space Comp = O(1)

def alt_efficient_leftmost_repeating_char(s):
    count = [False]*256
    res = -1
    for i in range(len(s)-1,-1,-1):
        if count[ord(s[i])]==True:
            res=i
        else:
            count[ord(s[i])]==True
    return res
#Tine Comp = O(n) - one traversal, Space Comp = O(1)


def leftmost_non_repeating_char(s):
    count = [0]*256
    for i in s:
        count[ord(i)] += 1
    for x in range(len(s)):
        if count[ord(s[i])]==1:
            return i
    return -1
#Tine Comp = O(n) - two traversal, Space Comp = O(1)

def efficient_leftmost_non_repeating_char(s):
    import sys
    count = [-1]*256
    res= sys.maxsize
    for i in range(len(s)-1,-1,-1):
        if count[ord(s[i])]==-1:
            count[ord(s[i])] = i        
        else:
            count[ord(s[i])] = -2
    for i in range(256):
        if count[i] >-1:
            res = min(res,count[i])
    if res == sys.maxsize:
        return -1
    else:
        return res
#Tine Comp = O(n) - one traversal as other traversal runs for constant time and not O(n) time, Space Comp = O(1) 256 is constant, so O(1)

def inbuilt_reverse_words_in_string(s):
    arr = s.strip().split()
    arr.reverse()
    return " ".join(arr)

def reverse_words_in_string(s):
    l = list(s)
    b = 0
    for x in range(len(l)):
        if l[x]==" ":
            reverse(l,b,x-1)
            b = x+1
    reverse(l, b, x)
    reverse(l, 0, len(l)-1)
    return("".join(l))
    
def reverse(l, b, x):
    while b<x:
        l[b], l[x] = l[x], l[b]
        b += 1
        x -= 1
#Time Comp = O(n) - two traversal, Space Comp = O(1)

print(reverse_words_in_string("He is a psycho"))
#print(recursive_check_subsequence("GEEKSFORGEEKS","GRGES   ", 0, 0))
#print(check_palindrome_short("racecaR"))
#check_rotation("ABCD","CDBA")
#reverse_string("stardom")