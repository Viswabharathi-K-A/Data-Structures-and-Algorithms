class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None

'''  
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
'''  

def insert_at_begin(head, k):
    temp = Node(k)
    if head!=None:
        head.prev = temp
    temp.next = head
    return temp

def insert_at_end(head, k):
    temp = Node(k)
    if head==None:
        return temp
    else:
        curr = head
        while curr.next!=None:
            curr = curr.next
        curr.next = temp
        temp.prev = curr
        return head

def del_head(head):
    if head==None or head.next==None:
        return None
    else:
        head = head.next
        head.prev = None
        return head

def del_last(head):
    if head==None or head.next==None:
        return None
    curr = head
    while curr.next.next!=None:
        curr=curr.next    
    curr.next=None
    return head

def reverse_dll(head):
    curr = head
    prev = None
    while curr!=None:
        curr.prev, curr.next = curr.next, curr.prev
        prev = curr
        curr = curr.prev
    return prev


def traverse_dll(head):
    curr = head
    while curr!=None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


head=None
head = insert_at_end(head, 5)
head = insert_at_end(head, 10)
head = insert_at_end(head, 15)
head = insert_at_begin(head, 0)
traverse_dll(head)
head = reverse_dll(head)
traverse_dll(head)


