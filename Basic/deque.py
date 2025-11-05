from collections import deque
'''
d = deque()
d.append(5)
d.append(10)
d.appendleft(0)
print(d)
print(d.popleft())
print(d.pop())
print(d)
d.extend([10,10,20])
print(d.count(10))
d.extendleft([-10,-5])
print(d)
d.rotate(1)
d.rotate(-2)
d.reverse()
print(d)
'''

class MyDeque:                      #using circular list
    def __init__(self,x):
        self.max = x
        self.deq = [None]*x
        self.front = 0
        self.sz = 0
    
    def insertFront(self,x):
        if self.sz == self.max:
            return
        else:
            self.front = (self.front-1)%self.max
            self.deq[self.front] = x
            self.sz += 1
    
    def insertRear(self,x):
        if self.sz == self.max:
            return
        else:
            rear = (self.front+self.sz-1)%self.max
            rear = (rear+1)%self.max
            self.deq[rear] = x
            self.sz += 1

    def deleteFront(self):
        if self.sz == 0:
            return 
        else:
            val = self.deq[self.front]
            self.front = (self.front+1)%self.max
            self.sz -= 1
            return val
    
    def deleteRear(self):
        if self.sz == 0:
            return  
        else:
            rear = (self.front+self.sz-1)%self.max
            val = self.deq[rear]
            self.sz -= 1
            return val
        
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return self.sz==0
    
    def getFront(self):
        return self.deq[self.front] if self.sz != 0 else None
    
    def getRear(self):
        rear = (self.front+self.sz-1)%self.max
        return self.deq[rear] if self.sz != 0 else None


    





class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class MyDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0

    def insertFront(self,x):
        temp = Node(x)
        if self.front == None:
            self.rear = temp
        else:
            self.front.prev = temp
            temp.next = self.front
        self.front = temp
        self.sz += 1

    def insertRear(self,x):
        temp = Node(x)
        if self.rear==None:
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
        self.rear = temp
        self.sz += 1

    def deleteFront(self):
        if self.front==None:
            return None
        else:
            val = self.front.key
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -= 1
            return val
        
    def deleteRear(self):
        if self.rear == None:
            return None
        else:
            val = self.rear.key
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            self.sz -= 1
            return val
    
    def getFront(self):
        return self.front.key if self.front else None
    
    def getRear(self):
        return self.rear.key if self.rear else None
    
    def isEmpty(self):
        return True if self.sz==0 else False
    
    def size(self):
        return self.sz
    
#Function to erase the element from specified position X in deque.
def eraseAt(deq,x):
    #code 
    deq.rotate(-x)
    deq.popleft()
    deq.rotate(x)
    
    
#Function to erase the elements in range start (inclusive), end (exclusive).
def eraseInRange(deq,s,e):
    #code here
        if s==e:
            return
        rot = s
        deq.rotate(-s)
        while rot!=e:
            deq.popleft()
            rot += 1
        deq.rotate(s)


