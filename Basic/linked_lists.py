class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

'''
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp1.next = temp2
temp2.next = temp3
head = temp1
'''




def linked_list_traversal(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next
#Time Comp = Theta(n) Aux Space = O(1)

def search_linked_list(head, n):
    curr = head
    pos = 1
    while curr != None:
        if curr.key == n:
            return pos
        curr = curr.next
        pos += 1
    return -1
#Time Comp = O(n) Aux Space = O(1)

def insert_at_beginning_ll(head,n):
    temp = Node(n)
    temp.next = head
    return temp
#Time Comp = O(1) Aux Space = O(1)

def insert_at_end_ll(head,n):
    temp = Node(n)
    if head==None:
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = temp
    return head
#Time Comp = O(n) Aux Space = O(1)


def ins_at_pos_ll(head,pos,n):
    temp = Node(n)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for x in range(1,pos-1):
        if curr == None:
            return head
        curr = curr.next
    temp.next = curr.next
    curr.next = temp
    return head
#Time Comp = Theta(min(n,pos)) Aux Space = O(1)

def delete_first_node(head):
    if head==None:
        return None
    else:
        return head.next
#Time Comp = O(1) Aux Space = O(1)

def delete_last_node(head):
    if head==None or head.next==None:
        return None
    curr = head
    while curr.next.next!=None:
        curr = curr.next
    curr.next=None
    return head
#Time Comp = O(n) Aux Space = O(1)


def delete_nth_node(ptr):                        #head pointer is not given, instead the reference to the node to be deleted is given.
    temp = ptr.next
    ptr.key = temp.key
    ptr.next = temp.next

def sorted_insert_in_linked_list(head,data):
    temp = Node(data)
    if head==None:
        return temp
    elif head.key>data:
        temp.next = head
        return temp
    curr = head
    while curr.next != None and curr.next.key<data:
        curr = curr.next
    temp.next = curr.next 
    curr.next = temp
    return head
#Time Comp = O(n) Aux Space = O(1)

def naive_middle_of_ll(head):
    if head == None:
        return None
    else:
        count = 0
        curr=head    
        while curr != None:
            curr = curr.next
            count += 1
        curr=head
        for i in range(count//2):
            curr = curr.next
        return curr.key
#Time Comp = O(n), two traversals Aux Space = O(1)

def middle_of_ll(head):
    if head==None:
        return None
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    return slow.key
#Time Comp = O(n), one traversal Aux Space = O(1)

def nth_node_from_end(head,n):
    count = 0
    curr = head
    while curr != None:
        count += 1
        curr = curr.next
    if n>count:
        return None
    curr = head
    for i in range(count-n):
        curr = curr.next
    return curr.key

def alt_nth_node_from_end(head,n):
    first = head
    sec = head
    for i in range(n):
        if sec==None:
            return None
        sec = sec.next
    while sec != None:
        sec = sec.next
        first= first.next
    return first.key

def remove_duplicates_from_sorted_ll(head):
    if head==None:
        return None
    curr = head.next
    temp = head
    while curr != None:
        if temp.key != curr.key:
            temp = temp.next
            temp.key = curr.key
        curr = curr.next
    temp.next=None

def alt_remove_duplicates_from_sorted_ll(head):
    curr = head
    while curr != None and curr.next!= None:
        if curr.key == curr.next.key:
            curr.next = curr.next.next
        else:
            curr = curr.next

def naive_reverse_ll(head):
    curr = head
    stack = []
    while curr!=None:
        stack.append(curr.key)
        curr = curr.next
    curr = head
    while curr!=None:
        curr.key = stack.pop()
        curr = curr.next
    return head

def reverse_ll(head):
    curr = head
    prev = None
    while curr!= None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def recursive_reverse_one(head):
    if head == None:
        return head
    if head.next==None:
        return head
    rest_head = recursive_reverse_one(head.next)
    temp = head.next
    temp.next = head
    head.next = None
    return rest_head
#Time Comp = O(n), Aux Space = O(n)

def recursive_reverse_two(curr,prev = None):
    if curr==None:
        return prev
    next = curr.next
    curr.next = prev
    return recursive_reverse_two(next,curr)
#Time Comp = O(n), Aux Space = O(n)

#Alternate initialisation
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(40)
#head.next.next.next.next.next = Node(40) 
#head.next.next.next.next.next.next = Node(40)    

'''
search_linked_list(head,10)

head = None
head = insert_at_beginning_ll(head,10)
head = insert_at_beginning_ll(head,20)
head = insert_at_beginning_ll(head,30)

head = None
head = insert_at_end_ll(head,10)
head = insert_at_end_ll(head,20)
head = insert_at_end_ll(head,30)
linked_list_traversal(head)

head = alt_ins_at_pos_ll(head,6,25)

head = delete_first_node(head)

head = delete_last_node(head)

head = sorted_insert_in_linked_list(head,45)

linked_list_traversal(head)

print(middle_of_ll(head))
'''

heads = recursive_reverse_two(head)
linked_list_traversal(heads)


    