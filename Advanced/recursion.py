#1 rope cutting problem
def rope_cutting(n,a,b,c):
    if n==0:
        return 0
    if n<0:
        return -1
    res = max(rope_cutting(n-a,a,b,c),rope_cutting(n-b,a,b,c),rope_cutting(n-c,a,b,c))
    if res==-1:
        return -1
    return res+1

#2 All subsets of string

def subset_of_given_string(str,curr,ind):
    if ind==len(str):
        print(curr)
        return
    subset_of_given_string(str,curr,ind+1)
    subset_of_given_string(str,curr+str[ind],ind+1)    

'''  In case if we want all the power set values to be returned as a list
def set(s,curr,ind):
    if ind==len(s):
        return [curr]
    return set(s,curr,ind+1) + set(s,curr+s[ind],ind+1)

'''
    
#3 Tower of Hani

def TOH(n,a,b,c):
    if n==1:
        print("Move ",n," from ",a," to ",c)
    else:
        TOH(n-1,a,c,b)
        print("Move ",n," from ",a," to ",c)
        TOH(n-1,b,a,c)  

#4 Josephus
def josephus(n,k):
    if n==1:
        return 0
    return (josephus(n-1,k)+k)%n   

#5 Subset Sum problem
def subset_sum(arr,n,sum):
    if n==0:
        return 1 if sum==0 else 0
    return subset_sum(arr,n-1,sum) + subset_sum(arr,n-1,sum-arr[n-1])

#6 Printing all Permutations
def per(s,i):
    n = len(s)
    if i==n-1:
        print(s)
        return
    for j in range(i,n):
        s[i], s[j] = s[j], s[i]
        per(s,i+1)
        s[i], s[j] = s[j], s[i]


# Possible words from phone digits

def possibleWords(numbers):
    d = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    return comb(numbers,d,"",0)
        
def comb(s,d,curr,j):
    if j==len(s):
        return [curr]
    res = []
    for i in d[s[j]]:
        res += comb(s,d,curr+i,j+1)
    return res


print(subset_sum([10,5,2,3,6],0,0,8,0))