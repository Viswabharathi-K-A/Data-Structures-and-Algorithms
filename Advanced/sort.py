import math
def lomuto(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] < pivot:
            i = i+1
            arr[j], arr[i] = arr[i], arr[j]
    arr[h], arr[i+1] = arr[i+1], arr[h]
    return i+1

def hoare(arr,l,h):
    pivot = arr[l]
    low =l-1
    high=h+1
    while True:
        low += 1
        while arr[low]<pivot:
            low +=1
        high-=1
        while arr[high]>=pivot:
            high-=1
        if low>high: 
          return high
        arr[low], arr[high] = arr[high], arr[low]




# Quick Sort Tail call elimination
def qSort(arr,l,h):
    while l<h:
        p = lomuto(arr,l,h)
        qSort(arr,l,p)
        l=p+1


#kth smallest element - Quick Select

def kthSmallest(arr, k):
    l = 0
    h = len(arr)-1
    while l<=h:
        p = lomuto(arr,l,h)
        if p == k-1:
            return arr[p]
        elif p > k-1:
            h = p-1
        else:
            l = p+1
    return -1

# Worst Case = O(n*n), Average Case = O(n)


#Min difference
def min_diff(arr):
    arr.sort()
    res = math.inf
    for i in range(1,len(arr)):
        res = min(res,arr[i]-arr[i-1])
    return res


#Chocolate distribution problem

def dist(arr,m):
    arr.sort()
    res = math.inf
    for i in range(m-1,len(arr)):
        res = min(res,arr[i]-arr[i-m+1])
    return res

#Sort an array with three types of elements
def three_type_sort(arr, pivot):
    low,mid,high = 0,0,len(arr)-1
    while mid<=high:
        if arr[mid]<pivot:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid]==pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    print(arr)


print(three_type_sort([0,1,0,2,1,2], 1))

#Merge overlapping intervals







