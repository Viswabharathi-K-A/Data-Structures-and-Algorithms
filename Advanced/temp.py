def f(numbers):
    d = {2:"ABC",3:"DEF",4:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ"}
    return x(numbers,d,"",0)

def x(s,d,curr,j):
    if j==len(s):
        return[curr]
    
    res = []
    for i in d[s[j]]:
        res += x(s,d,curr+i,j+1)
    return res

#print(f([2,3,7]))


'''
d = {2:"ABC",3:"DEF",4:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ"}
s = [2,3]
curr = ""
for i in d[s[0]]:
    curr += i
print(curr)
'''

def naive_partition_two_subset_sum(l, sum, target, i):
    if i==len(l):
        return False
    if sum > target:
        return False
    if sum==target:
        return True

    return naive_partition_two_subset_sum(l, sum+l[i], target, i+1) or naive_partition_two_subset_sum(l, sum, target, i+1)

def naive_longest_increasing_subsequence(l, i, seq):
    if i==len(l):
        print(seq)
        return
    naive_longest_increasing_subsequence(l, i+1, seq)
    naive_longest_increasing_subsequence(l, i+1, seq + [l[i]])

naive_longest_increasing_subsequence([1,3,4],0,[])
