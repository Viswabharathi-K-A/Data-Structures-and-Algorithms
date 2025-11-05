from collections import deque
'''
q = []
q.append(10)
q.append(20)
q.pop(0)
q.append(30)
print(q)
print(len(q))
print(q[0])
print(q[-1])
'''

'''

q = deque()
q.append(10)
q.append(20)
print(q.popleft())
q.append(30)
print(q)
print(len(q))
print(q[0])
print(q[-1])
'''

class MyQueue:        # using linked list
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0

    def enque(self,x):
        temp = Node(x)
        if self.rear==None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz += 1
    
    def deque(self):
        if self.front==None:
            print("Queue is Empty")
        else:
            val = self.front.key
            self.front = self.front.next
            if self.front==None:
                self.rear=None
            self.sz -= 1
            return val
    
    def getFront(self):
        return None if self.front == None else self.front.key
      
    def getRear(self):
        return None if self.rear == None else self.rear.key

    def isEmpty(self):
        return True if self.sz==0 else False
   
    def size(self):
        return self.sz
    
    def printlist(self):
        curr = self.front
        print("print ", end=" ")
        while curr!=None:
            print(curr.key, end=" ")
            curr=curr.next
        print()
       


class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyQueue:                #using circular list
    def __init__(self,x):
        self.cap = x
        self.queue = [None]*x
        self.front = 0
        self.sz = 0

    def enque(self,x):
        if self.sz==self.cap:
            print("Queue is full")
        else:
            rear = (self.front + self.sz -1)%self.cap
            rear = (rear+1)%self.cap
            self.queue[rear] = x
            self.sz += 1

    def deque(self):
        if self.sz==0:
            print("Queue is empty")
        else:
            val = self.queue[self.front]
            self.front = (self.front+1)%self.cap
            self.sz -= 1
            return val
    
    def getFront(self):
        return None if self.sz==0 else self.queue[self.front]
    
    def getRear(self):
        return None if self.sz==0 else self.queue[(self.front+self.sz-1)%self.cap]
    
    def size(self):
        return self.sz






class AltMyQueue:           #using circular list
    def __init__(self,x):
        self.max = x
        self.queue = [None]*self.max
        self.front = None
        self.rear = None
        self.sz = 0

    def enque(self,x):
        if self.rear==None:
            self.rear=0
            self.front=0
            self.queue[self.rear] = x
            self.sz += 1
        elif (self.rear+1)%self.max==self.front:
            print("Queue is full")
        else:
            self.rear = (self.rear+1)%self.max
            self.queue[self.rear] = x
            self.sz += 1

    def deque(self):
        if self.front==None:
            print("Queue is empty")
        else:
            val = self.queue[self.front]
            self.queue[self.front] = None
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front = (self.front+1)%self.max
            self.sz -= 1
            return val
    
    def size(self):
        return self.sz
    
    def getFront(self):
        return None if self.front == None else self.queue[self.front]
    
    def getRear(self):
        return None if self.rear == None else self.queue[self.rear]
    
    def isEmpty(self):
        return True if self.sz==0 else False


class Stack_using_Queue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0] if self.q1 else None

    def size(self):
        return len(self.q1)




    
'''
q = MyQueue()
q.enque(10)
q.enque(20)
q.enque(30)
print(q.deque())
print(q.size())
q.enque(40)
print(q.getFront())
print(q.getRear())
print(q.isEmpty())


q = MyQueue(5)
q.enque(10)
q.enque(20)
q.enque(30)
q.enque(40)
q.enque(50)
q.enque(60)
print(q.deque())
print(q.size())
q.enque(40)
print(q.getFront())
print(q.getRear())
'''

q = Stack_using_Queue()
q.push(5)
q.push(6)
print(q.pop())
q.push(7)
print(q.size())
q.push(8)
print(q.top())
