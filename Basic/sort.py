def optimised_bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if swapped == False:
            return l
    return l
#TimeComp : Worst = O(n*n), Best = O(n) (when it is sorted). Space comp = O(1)

def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1,n):
            if l[min_ind]>l[j]:
                min_ind = j
        l[i], l[min_ind] = l[min_ind], l[i]
    return l
#TimeComp = O(n*n), SpaceComp = O(1)

def alt_insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        temp = l[i]
        for j in range(i-1, -1, -1):
            if temp < l[j]:
                l[j+1] = l[j]
            else:
                l[j+1] = temp
                break
            l[j] = temp
    return l

def insertion_sort(l):
    for i in range(1,len(l)):
        temp = l[i]
        j = i-1
        while j>=0 and temp<l[j]:
            l[j+1]=l[j]
            j = j-1
        l[j+1] = temp
    return l
#TimeComp : Worst = O(n*n) (when it is reverse sorted) Best = O(n) (when it is sorted), Space Comp = O(1)

def merge_sorted_arrays(l1, l2):
    i=0
    j=0
    c = []
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            c.append(l1[i])
            i = i+1
        else:
            c.append(l2[j])
            j = j+1  
    while i < len(l1):
        c.append(l1[i])
        i = i+1
    while j < len(l2):
        c.append(l2[j])
        j = j+1

    return c   
#TimeComp = O(m+n) SpaceCOmp = O(m+n)

def merge_subarrays(a, low, mid, high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]
    i = 0
    j = 0
    k = low
    while i<len(left) and j<len(right):
        if left[i]<= right[j]:                       #("=" is there to maintain stability of the algorithm)
            a[k] = left[i]
            i = i+1
        else:
            a[k] = right[j]
            j = j+1
        k = k+1
    while i<len(left):
            a[k] = left[i]
            k = k+1
            i = i+1
    while j<len(right):
            a[k] = right[j]
            k = k+1
            j = j+1
#TimeComp = O(m+n) SpaceCOmp = O(m+n)

def mergeSort(a, l, r):
    if l<r:
        m = (l+r)//2
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge_subarrays(a, l, m, r)
#TimeComp = O(n*logn) AuxSpace = O(n)

def naive_union_of_sorted_arrays(l1, l2):
    l3 = l1 + l2
    l3.sort()
    for i in range(len(l3)):
        if i==0 or l3[i]!=l3[i-1]:
            print(l3[i], end=" ")
#TimeComp = O((m+n)*log(m+n)) AuxSpace = O(m+n)

def union_of_sorted_arrays(l1, l2):
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if  i>0 and l1[i]==l1[i-1]:
            i = i+1
        elif j>0 and l2[j]==l2[j-1]:
            j = j+1
        elif l1[i]<l2[j]:
            print(l1[i], end=" ")
            i=i+1
        elif l2[j]<l1[i]:
            print(l2[j], end=" ")
            j=j+1
        else:                                               #(l1[i]==l2[j])
            print(l1[i], end=" ")
            i=i+1
            j=j+1
    while i<len(l1):
        if i>0 and l1[i]!=l1[i-1]:
            print(l1[i], end=" ")
        i=i+1
    while j<len(l2):
        if j>0 and l2[j]!=l2[j-1]:
            print(l2[j], end=" ")
        j=j+1
#TimeComp = O(m+n) AuxSpace = O(1)

def naive_intersection_of_sorted_arrays(l1,l2):
    for i in range(len(l1)):
        if i>0 and l1[i]==l1[i-1]:
            continue
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                print(l1[i], end=" ")
                break
#TimeComp = O(m*n) AuxSpace = O(1)

def intersection_of_sorted_arrays(l1,l2):
    i=0
    j=0
    while i<len(l2) and j<len(l2):
        if i>0 and l1[i]==l1[i-1]:
            i=i+1
        elif l1[i]<l2[j]:
            i=i+1
        elif l2[j]<l1[i]:
            j=j+1
        else:
            print(l1[i], end=" ")
            i=i+1
            j=j+1  
#TimeComp = O(m+n) AuxSpace = O(1)

def number_of_inversions(a, l, r):
    res = 0
    if l<r:
        mid=(l+r)//2
        res  += number_of_inversions(a,l,mid)
        res  += number_of_inversions(a,mid+1,r)
        res  += count_pair(a, l, mid, r)
    return res
def count_pair(a,l,m,r):
    count=0
    left = a[l:m+1]
    right=a[m+1:r+1]
    x = l
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            a[x] = left[i]
            i=i+1
        else:
            a[x]=right[j]
            j=j+1
            count = count+ len(left)-i
        x=x+1
    while i<len(left):
        a[x]=left[i]
        x=x+1
        i=i+1
    while j<len(right):
        a[x]=right[j]
        j=j+1
        x=x+1
    return count
#TimeComp = O(n*logn) AuxSpace = O(n)

def lomuto_partition(arr, l, h):
    i = l-1
    pivot = arr[h]
    for j in range(l,h):
        if pivot>arr[j]:
            i=i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1
#TimeComp = O(n) AuxSpace = O(1)
    
def hoares_partition(a, l, h):
    pivot = a[l]
    i = l-1
    j = h+1
    while True:
        i=i+1
        while a[i]<pivot:
            i=i+1
        j=j-1
        while a[j]>pivot:
            j=j-1
        if i>=j:
            return j
        a[i], a[j] = a[j], a[i]
#TimeComp = O(n) AuxSpace = O(1)

def qSort_lomuto(arr, l, h):
    if l<h:
        p = lomuto_partition(arr,l,h)
        qSort_lomuto(arr,l,p-1)
        qSort_lomuto(arr,p+1,h)
#TimeComp = Average:O(n*logn); Worst:O(n*n) AuxSpace = O(1)

def counting_sort(arr, n):
    count = [0]*(n+1)            #n is the largest element in the list, so the count array should be from 0 to n-(n+1)elements
    res = [0]*len(arr)
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1,n+1):
        count[i] =  count[i-1] + count[i]               #making the count array as cumulative array to get the index of each element

    for i in range(len(arr)-1,-1,-1):
        res[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return res  
#TimeComp = O(n) AuxSpace = O(n)


print(counting_sort([1,3,2,3,4,0,1,4,4,1,2], 4))
            
'''
arr = [8,9,11,2,5,10]
print(number_of_inversions(arr, 0, 5))
print(arr)
'''