def linear_search(l, x):
    for i in range(len(l)):
        if x is l[i]:
            return i
    return -1
#TimeComp = O(n) SpaceComp = O(1)


def binary_search(l, x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid] == x:
            return mid
        elif l[mid]<x:
            low = mid+1
        elif l[mid]>x:
            high = mid-1
    return -1
#TimeComp = O(logn) SpaceComp = O(1)

def rec_bsearch(l, x, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if l[mid]==x:
        return mid
    elif l[mid]>x:
        return rec_bsearch(l, x, low, mid-1)
    elif l[mid]<x:
        return rec_bsearch(l, x, mid+1, high)
#TimeComp = O(logn) SpaceComp = O(logn)

def rec_first_occurrence_index(l, x, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if l[mid]>x:
        return rec_first_occurrence_index(l, x, low, mid-1)
    elif l[mid] <x:
        return rec_first_occurrence_index(l, x, mid+1, high)
    else:
        if mid == 0 or l[mid]!= l[mid-1]:
            return mid
        return rec_first_occurrence_index(l, x, low, mid-1)
 #TimeComp = O(logn) SpaceComp = O(logn)   

def first_occurrence_index(l, x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (high+low)//2
        if l[mid]<x:
            low = mid+1
        elif l[mid]>x:
            high = mid-1
        else:
            if mid == 0 or l[mid]!=l[mid-1]:
                return mid
            high = mid-1
    return -1
#TimeComp = O(logn) SpaceComp = O(1)

def rec_last_occurrence_index(l, x, low, high):
    if low>high:
        return -1
    mid = (low+high)//2
    if l[mid]>x:
        return rec_last_occurrence_index(l, x, low, mid-1)
    elif l[mid]<x:
        return  rec_last_occurrence_index(l, x, mid+1, high)
    else:
        if mid==len(l)-1 or l[mid]!=l[mid+1]:
            return mid
        else:
            return rec_last_occurrence_index(l, x, mid+1, high)

def last_occurrence_index(l, x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (high+mid)//2
        if l[mid]<x:
            low = mid+1
        elif l[mid]>x:
            high = mid-1
        else:
            if mid == len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low = mid+1
    return -1

def count_occurrence(l,x):
    f = first_occurrence_index(l,x)
    if f == -1:
        return 0
    else:
        return last_occurrence_index(l, x) - f + 1

def naive_square_root_floor(x):
    i=1
    while i*i<=x:
        i+= 1
    return i-1
 #TimeComp = O(sqrt(x)) SpaceComp = O(1)

def square_root_floor(x):
    low = 1
    high = x
    ans = -1
    while low<=high:
        mid = (low+high)//2
        sqrt = mid*mid
        if sqrt == x:
            return mid
        elif sqrt > x:
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return ans
#TimeComp = O(logn) SpaceComp = O(1)
            

    
print(square_root_floor(25))
      