

def avg(a):
    sum = 0
    for x in a:
        sum += x
    return sum/len(a)
#TimeComp = O(n) 

def seg_even_odd(l):
    even = []
    odd = []
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd #returns as a tuple

def smaller_than_x(l,n):
    small = []
    for x in l:
        if x<n:
            small.append(x)
    return small

def largest(l):
    big = l[0]
    for x in l:
        if x>big:
            big = x
    return big

def sec_largest(l):
    if len(l)<=1:
        return 
    big1 = l[0]
    big2 = None
    for x in l:
        if x>big1:
            big2 = big1
            big1 = x
        elif x!=big1:
            if big2 == None or big2<x:
                big2 = x
    return big2

def check_if_sorted(l):
    if len(l)<=1:
        return True
    for i in range(len(l)-1):
        if l[i+1]-l[i]>=0:
            pass
        else:
            return False
    return True

def reverse_list(l):
    s = 0
    e = len(l)-1
    while s<e:
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1
    return l

def naive_number_of_non_duplicates_sortedList(l):
    temp = [0]*len(l)
    temp[0] = l[0]
    res = 0
    for i in range(1,len(l)):
        if temp[res] != l[i]:
            temp[res+1] = l[i]
            res += 1
    return res+1
#TimeComp = O(n) SpaceComp = O(n)

def number_of_non_duplicates__sortedlist(l):
    res = 1
    for i in range(1,len(l)):
        if l[res-1]!=l[i]:
            l[res]=l[i]
            res += 1
    return res
#TimeComp = O(n) SpaceComp = O(1)

def rotate_list_left_by1(l):
    temp = l[0]
    for x in range(1,len(l)):
        l[x-1] = l[x]
    l[len(l)-1] = temp
    return l



def one_odd_occurring(l):
    l.sort()
    print(l)
    res = 0
    count = 1
    for i in range(1,len(l)):
        if l[res]!=l[i]:
            if count%2 != 0:
                return l[res]
            res = i
            count = 1
        elif l[res]==l[i]:
            count += 1

def efficient_one_odd_occurring(arr) :   
    res = 0    
    for i in arr :
        res = res ^ i        
    return res
    
    


# statement 2

print(one_odd_occurring([1,2,1,3,4,2,5,5,3]))