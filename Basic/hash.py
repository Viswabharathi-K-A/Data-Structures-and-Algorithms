class myhash_chaining:
    def __init__(self,size):
        self.bucket = size #hashfucntion = key%bucket
        self.hash_table = [[] for _ in range(self.size)]
    def insert(self, n):
        self.hash_table[n%self.bucket].append(n)

    def delete(self, n):
        self.hash_table[n%self.bucket].remove(n)

    def search(self, n):
        return n in self.hash_table[n%self.bucket]
    
class myhash_openAddressing:
    def __init__(self, n):
        self.bucket = n
        self.arr = [-1 for _ in range(n)]
        self.size = 0

    def hash(self, n):
        return n%self.bucket

    def search(self, n):
        i = self.hash(n)
        j = i
        while self.arr[j] != -1:
            if self.arr[j] == n:
                return True
            j = (j+1)%self.bucket
            if j==i:
                return False
        return False

    def insert(self,n):
        i = self.hash(n)
        if self.size==self.bucket:
            return False
        if self.search(n) == True:
            return False
        while self.arr[i] != -1 or self.arr[i]==-2:
            i = (i+1)%self.bucket
        self.arr[i]=n
        self.size += 1

    def remove(self, n):
        i = self.hash(n)
        j = i 
        if self.size==0:
            return False  
        while self.arr[j] != -1:
            if self.arr[j] == n:
                self.arr[j] = -2
                self.size -= 1
                return True
            j = (j+1)%self.bucket
            if j==i:
                return False
        return False        
               
def naive_frequency_all_elements(arr):
    for x in range(len(arr)):
        flag=False
        for j in range(x):
            if arr[j]==arr[x]:
                flag=True
                break
        if flag==True:
            continue
        else:
            freq=1
            for j in range(x+1,len(arr)):
                if arr[j]==arr[x]:
                    freq +=1
            print(arr[x], freq)

def naive_frequency_all_elements_2(arr):
    arr.sort()
    temp = arr[0]
    count=1
    for i in range(1,len(arr)):
        if temp==arr[i]:
            count += 1
        else:
            print(temp, count)
            count=1
            temp=arr[i]
    print(temp,count)

def freq_all_elements(arr):
    freq=dict()
    for x in arr:
        if x in freq.keys():
            freq[x] += 1
        else:
            freq[x]=1
    for x in freq:
        print(x, freq[x])


def naive_count_distinct_elements_list(l):
    res=1
    for x in range(1,len(l)):
        if l[x] not in l[0:x]:
            res += 1
    return res

def count_distinct_elements_list(l):
    return len(set(l))

print(count_distinct_elements_list([1,4,2,6,4,6,3,2]))
     

"""
h = myhash_openAddressing(7)
h.insert(49)
h.insert(56)
print(h.search(56))
h.remove(56)
print(h.remove(56))
print(h.arr)
"""