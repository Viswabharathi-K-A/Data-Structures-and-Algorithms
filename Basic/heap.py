import math


class MyMinHeap:
#    def __init__(self):          NO build heap
#        self.arr = []

    def __init__(self, l=[]):
        self.arr = l
        i = (len(l)-2)//2
        while i>=0:
            self.heapify(i)
            i -= 1
    
    def parent(self,i):
        return (i-1)//2
    
    def lchild(self,i):
        return 2*i+1
    
    def rchild(self,i):
        return 2*i+2
    
    def insert(self,x):
        self.arr.append(x)
        i = len(self.arr)-1
        while i>0 and self.arr[self.parent(i)]>self.arr[i]:
            x = self.parent(i)
            self.arr[x], self.arr[i] = self.arr[x], self.arr[i]
            i = x
        
    def extractMin(self):
        n = len(self.arr)
        if n == 0:
            return math.inf
        min = self.arr[0]
        self.arr[0] = self.arr[n-1]
        self.arr.pop()
        self.heapify(0)
        return min
    
    def heapify(self,i):
        arr = self.arr
        lc = self.lchild(i)
        rc = self.rchild(i)
        n = len(self.arr)
        smallest = i
        if lc<n and arr[lc]<arr[smallest]:
            smallest = lc
        if rc<n and arr[rc]<arr[smallest]:
            smallest = rc
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.heapify(smallest)

    def decreaseKey(self,i,x):
        arr = self.arr
        n = len(arr)
        arr[i] = x
        while i>0 and arr[self.parent(i)]>arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p 
    
    def delete(self,i):
        n = len(self.arr)
        if i>=n:
            return
        else:
            self.decreaseKey(i, -math.inf)
            self.extractMin() 
    

#Heapsort, ascending order
def buildHeap(l):
    n = len(l)
    for i in range((n-2)//2, -1, -1):
        maxheapify(l,n,i)


def maxheapify(l,n,i):
    lchild = 2*i+1
    rchild = 2*i+2
    biggest = i
    if lchild<n and l[biggest]<l[lchild]:
        biggest = lchild
    if rchild<n and l[biggest]<l[rchild]:
        biggest = rchild
    if biggest != i:
        l[biggest], l[i] = l[i], l[biggest]
        maxheapify(l,n,biggest)

def heapSort(arr):
    n = len(arr)
    buildHeap(arr)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        maxheapify(arr,i,0)

'''
arr = [3,5,11,0,-2,12]
heapSort(arr)
print(arr)
'''

import heapq
pq = [3,4,1,7,0]
heapq.heapify(pq)
print(pq)
heapq.heappush(pq,-3)
print(pq)
heapq.heappop(pq)
print(pq)

print(heapq.nlargest(3,pq))
print(heapq.nsmallest(3,pq))

print(heapq.heappushpop(pq,7))
print(heapq.heapreplace(pq,9))
