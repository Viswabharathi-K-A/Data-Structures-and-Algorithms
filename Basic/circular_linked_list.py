class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

def traverse_circular_ll(head):
    if head==None:
        return
    print(head.key,end=" ")
    curr = head.next
    while curr!=head:
        print(curr.key,end=" ")
        curr = curr.next
#Time Comp = O(n), Aux Space = O(1)

def insert_at_begin(head,k):
    temp = Node(k)
    if head==None:
        temp.next=temp
        return temp
    curr = head
    while curr.next!=head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return temp
#Time Comp = O(n), Aux Space = O(1)

def eff_ins_at_begin(head,k):
    temp = Node(k)
    if head==None:
        temp.next=temp
        return temp    
    else:
        temp.next=head.next
        head.next=temp
        head.key, temp.key = temp.key, head.key
        return head
#Time Comp = O(1), Aux Space = O(1)

def ins_at_end(head,k):
    temp=Node(k)
    if head==None:
        temp.next=temp
        return temp
    curr = head
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return head
#Time Comp = O(n), Aux Space = O(1)

def eff_ins_at_end(head,k):
    temp = Node(k)
    if head==None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        temp.key, head.key = head.key, temp.key
        return temp
#Time Comp = O(1), Aux Space = O(1)

def delete_first(head):
    if head==None:
        return None
    elif head.next==head:
        return None
    else:
        curr = head
        while curr.next!=head:
            curr=curr.next
        curr.next = head.next
        return curr.next
#Time Comp = O(n), Aux Space = O(1)
#     
def eff_del_first(head):
    if head==None:
        return None
    elif head.next==head:
        return None
    else:
        temp = head.next
        head.key = temp.key
        head.next=temp.next
        return head
#Time Comp = O(1), Aux Space = O(1)

def del_kth_node(head,k):
    if head==None:
        return None
    elif k==1:
        if head.next==head:
            return None
        else:
            head.key = head.next.key
            head.next = head.next.next
            return head
    else:
        curr = head
        for _ in range(k-2):
            curr = curr.next
        curr.next=curr.next.next
        return head
#Time Comp = O(n), Aux Space = O(1)

traverse_circular_ll(head)
print()
heads = del_kth_node(head,1)
traverse_circular_ll(heads)