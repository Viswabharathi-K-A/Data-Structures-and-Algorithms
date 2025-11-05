class node:
    def __init__(self, val):
        self.key = val
        self.next = None

# Reverse a linked list in group ff k

# Recursive solution
def rev_ll_groups(head, k):
    curr = head
    prev, next = None, None
    count = 0
    while curr!=None and count<k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    if next!= None:
        rem_head = rev_ll_groups(curr ,k)
        head.next = rem_head
    return prev   
#Time Comp = O(n), Aux space = O(n/k)

#iterative solution
def rev_ll_group_itr(head, k):
    curr = head
    first_pass = True
    prev_first = None
    while curr!=None:
        first, prev = curr, None
        count = 0 
        while curr!=None and count<k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        if first_pass:
            first_pass = False
            head = prev
        else:
            prev_first.next = prev
        prev_first = first
        return head
#Time Comp = O(n), Aux space = O(1)


# Detect a loop in a linked list
def floyd_cycle_detection(head):
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False
#Time Comp = O(m+n), Aux space = O(1) - m: No of nodes that are not part of the cycle. n: No of nodes in the cycle

# Detect and remove a loop in linked list