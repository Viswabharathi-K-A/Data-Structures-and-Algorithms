import math 
'''
stack = []
stack.append(10)
stack.append(20)
print(stack.pop())
top = stack[-1]
print(top)
size = len(stack)
print(size)

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.sizes = 0

    def push(self, k):
        temp = Node(k)
        temp.next = self.head
        self.head = temp
        self.sizes += 1

    def pop(self):
        if self.head==None:
            return math.inf
        pop = self.head.key
        self.head = self.head.next
        self.sizes -= 1
        return pop

    def peek(self):
        if self.head==None:
            return math.inf
        return self.head.key
    
    def size(self):
        return self.sizes
    
s = MyStack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.pop())
s.push(40)
print(s.peek())
print(s.size())
'''

class Queue_using_Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def deque(self):
        if not self.s2:
            if not self.s1:
                return None
            while self.s1:
                self.s2.append(self.s1.pop())  
        return self.s2.pop()
    
    def  enque(self,x):
        self.s1.append(x)



s = Queue_using_Stack()
s.enque(1)
s.enque(2)
print(s.getFront())
print(s.getRear())
print(s.deque())
s.enque(3)
print(s.size())


def balanced_paranthesis(str):
    stack = []
    for x in str:
        if x in ('(','{','['):
            stack.append(x)
        else:
            if not stack:            # handles cases when the first element to be appended to the stack are '(', '{' or '['
                return False
            elif isMatching(stack[-1],x)==False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

def isMatching(a,b):
    if (a=='(' and b==')') or (a=='[' and b==']') or (a=='{' and b=='}'):
        return True
    else:
        return False

def InfixtoPostfix(s):
        #code here
        stack = []
        exp = []
        for x in s:
            if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122) or (ord(x)>=48 and ord(x)<=57):
                exp.append(x)
            else:
                if x in ('+','-'):
                    while stack != [] and stack[-1] in ('^','*','/','+','-'):
                        exp.append(stack.pop())
                    stack.append(x)
                elif x in ('*','/'):
                    while stack != [] and stack[-1] in ('^','*','/'):
                        exp.append(stack.pop())
                    stack.append(x) 
                elif x == '^':
                    while stack != [] and stack[-1] == '^':
                        exp.append(stack.pop())
                    stack.append(x)
                elif x == ')':
                    while stack[-1] != '(':
                        exp.append(stack.pop())
                    stack.pop()
                else:
                    stack.append(x)
        while stack:
            exp.append(stack.pop())
        return "".join(exp)

def preToInfix(self, pre_exp):
        # Code here
    stack = []
    for x in reversed(pre_exp):
        if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122) or (ord(x)>=48 and ord(x)<=57):
            stack.append(x)
        else:
            exp = '('+stack.pop()+x+stack.pop()+')'
            stack.append(exp)
    exp = stack.pop()
    return exp

#print(balanced_paranthesis('(){}[]'))
