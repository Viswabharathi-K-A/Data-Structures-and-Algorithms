class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

root = Node(30)
root.left = Node(20)
root.left.right = Node(25)
root.right = Node(40)
root.right.right = Node(60)
root.right.left = Node(35)

def search(root,val):
    if root==None:
        return False
    elif root.key == val:
        return True
    elif root.key>val:
        return search(root.left,val)
    else:
        return search(root.right,val)
#Time Comp = O(h) - height of tree, Aux Space = O(h)


def search_itr(root,val):
    curr = root
    while curr:
        if curr.key==val:
            return True
        elif root.key>val:
            curr = curr.left
        else:
            curr = curr.right
    return False
#Time Comp = O(h) - height of tree, Aux Space = O(1)

def insert(root,val):
    if root == None:
        return Node(val)
    elif root.key == val:
        return root
    elif root.key>val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root
    
def insert_itr(root,val):
    temp = Node(val)
    if root==None:
        return temp
    parent = None
    curr = root
    while curr:
        parent = curr
        if curr.key==val:
            return root
        elif curr.key>val:
            curr = curr.left
        else:
            curr = curr.right
    if parent.key<val:
        parent.right = temp
    else:
        parent.left = temp
    return root

def delete(root,val):
    if root==None:
        return root
    elif root.key>val:
        root.left = delete(root.left,val)
    elif root.key<val:
        root.right = delete(root.right,val)
    else:                                               # root.key matches with the value
        if not root.left and not root.right:            # if the node to be deleted is a leaf node
            return None
        elif not root.left:                             # If the node to be deleted has only right child                          
            return root.right
        elif not root.right:                            #If the node to be deleted has only left child
            return root.left
        else:
            succ = inorder_successor(root.right)        #replacing the value of the node to be deleted with the inorder successor, alternatively, this can be done with inorder predecessor too
            root.key = succ
            root.right = delete(root.right, succ)
        return root

def inorder_successor(curr):
    while curr.left:
        curr = curr.left
    return curr.key

def floor(root,val):
    curr = root
    floor = None
    while curr:
        if curr.key==val:
            return val
        elif curr.key>val:
            curr = curr.left
        else:
            floor = curr.key
            curr = curr.right
    return floor

def ceil(root,val):
    curr = root
    ceil = None
    while curr:
        if curr.key == val:
            return val
        elif curr.key<val:
            curr = curr.right
        else:
            ceil = curr.key
            curr = curr.left
    return ceil


root = delete(root,30)
print(search(root,30))
