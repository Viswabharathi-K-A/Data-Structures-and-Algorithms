import math
def binary_search(l,s,e,x):
    while s<=e:
        mid = (s+e)//2
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            e = mid-1
        else:
            s = mid+1
    return -1

def first_occurrence(l,x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid]>x:
            high = mid-1
        elif l[mid]<x:
            low = mid+1
        else:
            if mid==0 or l[mid]!=l[mid-1]:
                return mid
            else:
                high= mid-1

def last_occurrence(l,x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid]>x:
            high = mid-1
        elif l[mid]<x:
            low = mid+1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low = mid+1

#1 search in an infinite sorted array
def naive_searc_inf_sorted_array(l,x):
    i = 0
    while l[i]<=x:
        if l[i]==x:
            return i
        i += 1
    return -1

def search_inf_sorted_array(l,x):
    if l[0]==x:
        return 0
    i=1
    while l[i]<=x:
        if l[i]==x:
            return i
        i *= 2
    return binary_search(l,i//2+1,i-1,x)
#Time Comp = O(logn)


#2 search in sorted and rotated array
def search_rotate(l,x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid]==x:
            return mid
        elif l[low]<l[mid]:                  #left half sorted
            if l[0]<=x<l[mid]:
                high = mid-1
            else:
                low = mid+1
        else:                               #right half sorted
            if l[mid]<x<=l[high]:
                low = mid+1
            else:
                high = mid-1
    return -1
#Time Comp = O(logn)

#3 Find a peak element
def peak_element(l):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (high+low)//2
        if (mid==0 or l[mid]>=l[mid-1]) and (mid==len(l)-1 or l[mid]>=l[mid+1]):
            return mid
        if mid>0 and l[mid-1]>=l[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1
#Time Comp = O(logn)

#4 Count occurrences in a sorted array

def count_occ(l,x):
    x = first_occurrence(l,x)
    if x==-1:
        return 0
    else:
        return last_occurrence(l,x)-x+1 
    
#5 Two pointers approach, find a pair with sum x (Works well only if we have sorted array)

def pair(l,x):
    i=0
    j=len(l)-1
    while i<j:
        if l[i]+l[j]==x:
            return True
        elif l[i]+l[j]>x:
            j -= 1
        else:
            i += 1
    return False
#Time Comp: O(n)

#6 Triplet in a sorted array

def naive_triplet(l,x):
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            for k in range(j+1,len(l)):
                if l[i]+l[j]+l[k]==x:
                    return True
    return False

def triplet(l,x):
    for i in range(len(l)-2):
        sum = x-l[i]
        j=i+1
        k=len(l)-1
        while j<k:
            if l[j]+l[k]==sum:
                return True
            elif l[j]+l[k]>sum:
                k -= 1
            else:
                j += 1
    return False

#Time Comp = O(n*n)

#7 Median of sorted array 

def naive_median(l1,l2):
    n = len(l1)+len(l2)
    i, j = 0, 0
    arr = []
    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            arr.append(l1[i])
            i += 1
        else:
            arr.append(l2[j])
            j += 1
    while i<len(l1):
        arr.append(l1[i])
        i += 1
    while i<len(l2):
        arr.append(l2[j])
        j += 1
    if n%2==1:
        return arr[n//2]
    else:
        print(arr[n//2],arr[n//2+1])
        return (arr[n//2-1]+arr[n//2])/2

def median_sorted_arrays(l1,l2):
    n1 = len(l1)
    n2 = len(l2)
    if n2<n1:
        return median_sorted_arrays(l2,l1)
    low = 0
    high = n1
    while low<=high:
        mid = (low+high)//2
        leftASize = mid
        leftBSize = (n1+n2+1)//2 - leftASize

        leftA = l1[leftASize-1] if leftASize>0 else -math.inf
        leftB = l2[leftBSize-1] if leftBSize>0 else -math.inf
        rightA = l1[leftASize] if leftASize<n1 else math.inf
        rightB = l1[leftBSize] if leftBSize<n2 else math.inf

        if leftA<=rightB and leftB<=rightB:
            if (n1+n2)%2 == 1:
                return max(leftA,leftB)
            else:
                return (max(leftA,leftB)+min(rightA+rightB))/2.0
        elif leftA>rightB:
            high = mid - 1
        else:
            low = mid + 1

#8 Repeating element

def repeating_element(l):
    slow = l[0]
    fast = l[0]
    slow = l[slow]
    fast = l[l[fast]]
    while slow != fast:
        slow = l[slow]
        fast = l[l[fast]]
    slow = l[0]
    while slow!=fast:
        slow = l[slow]
        fast = l[fast]
    return slow
#Time Comp = O(n)


#9 allocate minimum pages
def naive_page_allocate(l,n,k):
    if k==1:
        return sum(l[0:n])
    if n==1:
        return l[0]
    res = float("inf")
    for i in range(1,n):
        left = naive_page_allocate(l,i,k-1)
        right = sum(l[i:n])
        curr_max = max(left,right)
        res = min(curr_max,res)
    return res
#Time Comp = O(2^n)

def minPage(l,k):
    n = len(l)
    s = sum(l)
    mx = max(l)
    low, high = mx, s
    res = high
    while low<=high:
        mid = (low+high)//2
        if (isFeasible(l,n,k,mid)):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res

def isFeasible(l,n,k,max_pages):
    students_required = 1
    current_sum = 0
    for page in l:
        if current_sum+page>max_pages:
            current_sum = page
            students_required += 1
        else:
            current_sum += page
    return (students_required<=k)

#Time Comp = O(n*log(sum-max))


"""
Given an integer array representing the heights of N buildings, the task is to delete N-2 buildings such that the water that can be trapped between the remaining two building is maximum.
Note: The total water trapped between two buildings is gap between them (number of buildings removed) multiplied by height of the smaller building.
"""
def maxWater(self, height, n): 
    #Your code here
    """
    res = 0
    for i in range(n):
        for j in range(n-1,i,-1):
            res = max(res,(j-i-1)*min(height[i],height[j]))
    return res   
        """
    res = 0
    i=0
    j=n-1
    while i<j:
        res = max(res,j-i-1*min(height[i],height[j]))
        gap -= 1
        if height[i]>height[j]:
            j=j-1
        else:
            i=i+1
    return res







print(median_sorted_arrays([1,2,3,4,5,6],[10,20,30,40,50]))
