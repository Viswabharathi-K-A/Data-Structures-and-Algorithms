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
'''
1 Detect loop using Floyd’s detection algorithm.
2 Move “slow-p” to the beginning of the linked list and keep “fast-p” at the meeting point.
3 Move one by one (slow and fast at same speed). The point where they meet now is the first node of the loop.
'''
def floyd_cycle_removal(head):
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow!=fast:
            return
    slow = head
    while slow.next!=fast.next:
            slow = slow.next
            fast = fast.next
    fast.next = None
    '''
    ### 
    **1. Setup**

    * Use two pointers:

    * `slow` → moves 1 step at a time
    * `fast` → moves 2 steps at a time
    * Both start from the head of the linked list.

    **2. Detecting a Loop**

    * Move both pointers forward at their respective speeds.
    * If `slow` and `fast` meet, a loop exists.
    * If `fast` or `fast.next` becomes `NULL`, there is no loop.

    **3. Before the First Meeting Point**
    Let:

    * `m` = distance from head to start of loop
    * `k` = distance from start of loop to meeting point
    * `n` = length of the loop
    * `x` = no. of rounds made by `slow` inside the loop
    * `y` = no. of rounds made by `fast` inside the loop

    **4. Distance Relation**
    Distance traveled by `slow` x 2 = Distance traveled by `fast`
    2 x (m + k + x·n) = m + k + y·n

    Simplify:
    m + k = n(y - 2x)

    ⇒ `(m + k)` is a multiple of `n`, meaning after moving `m` steps from the meeting point, you’ll reach the loop start.
    '''
            
# Intersection of two linked list
def int_ll_set(head1,head2):
    s = set()
    curr = head1
    while curr!=None:
        s.add(curr)
        curr = curr.next
    curr = head2
    while curr!=None:
        if curr in s:
            return curr.key
        curr = curr.next
    return -1

# Time comp = O(m+n) Space comp = O(m)

def int_ll(d, head1,head2): # d - differnece of size between the two linked list. head1 is always the head of the bigger linked list
    curr1 = head1
    curr2 = head2
    for i in range(d):
        if curr1==None:
            return -1
        curr1 = curr1.next
    while curr1!=None and curr2!=None:
        if curr1==curr2:
            return curr1.key
        curr1 = curr1.next
        curr2 = curr2.next
        

