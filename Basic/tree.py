from collections import deque
import math
class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None



def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.key, end =" ")
    inorder(root.right)
#Time Comp = Theta(n) -> no. of nodes, Aux Space = Theta(h) -> height of binary tree

def preorder(root):
    if root!=None:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)
#Time Comp = Theta(n) -> no. of nodes, Aux Space = Theta(h) -> height of binary tree

def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")
#Time Comp = Theta(n) -> no. of nodes, Aux Space = Theta(h) -> height of binary tree

def beg_height(root):
    if root==None:
        return 0                        #This will give the height in terms of nodes; if we want the height in terms of , then return -1 instead of 0. As nu. of edges = no. of nodes -1
    lh = beg_height(root.left)
    rh = beg_height(root.right)
    return max(lh,rh) + 1
#Time Comp = Theta(n) -> no. of nodes, Aux Space = Theta(h) -> height of binary tree

def height(root):
    if root == None:
        return 0
    return max(height(root.left),height(root.right)) + 1


def node_at_depthk(root,k):
    if root == None:
        return
    elif k==0:
        print(root.key, end=" ")
    else:
        node_at_depthk(root.left, k-1)
        node_at_depthk(root.right, k-1)
#Time Comp = O(n) -> no. of nodes, Aux Space = O(h) -> height of binary 


def naive_level_order(root):
    h = height(root)
    for i in range(0,h):
        node_at_depthk(root,i)
#Time Comp = O(n+nh) = O(nh) -> n is no. of nodes and h is height of tree

def level_order(root):   # use queue
    if not root:
        return
    d  = deque([root])
    while d:
        node  = d.popleft() 
        print(node.key, end = " ")
        if node.left!=None:
            d.append(node.left)
        if node.right!=None:
            d.append(node.right)    
#Time Comp = Theta(n) -> no. of nodes, Aux Space = O(n) (or to be precise Theta(w) as in w is the width of the binary tree)

def iter_preorder(root): #use stack
    if not root:
        return 
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.key, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
#Time comp = Theta(n), Aux Space = O(h)

def iter_inorder(root): #use stack
    if not root:
        return
    curr = root
    stack = []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            node = stack.pop()
            print(node.key, end=" ")
            curr = node.right
#Time comp = Theta(n), Aux Space = O(h)

def iter_postorder(root):  #use stack
    if not root:
        return
    stack = [root]
    ls = []
    while stack:
        node = stack.pop()
        ls.append(node.key)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    for i in reversed(ls):
        print(i, end=" ")

def post_order_last_visited(root): #use stack
    if not root:
        return
    stack = []
    last_vis = None
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            top = stack[-1]
            if top.right and top.right!=last_vis:
                curr = top.right
            else:
                print(top.key, end=" ")
                last_vis = stack.pop()


def size_bin_tree(root):
    if root == None:
        return 0
    return size_bin_tree(root.left) + size_bin_tree(root.right) + 1
    # lm = size_bin_tree(root.left)
    # rm = size_bin_tree(root.right)
    # return lm+rm+1    

def max_bin_tree(root):
    if root==None:
        return -math.inf
    return max(max_bin_tree(root.left),max_bin_tree(root.right),root.key)
    # lm = max_bin_tree(root.left)
    # rm = max_bin_tree(root.right)
    # return max(lm,rm,root.key)

def isIdentical(self,r1, r2):
        # Code here
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return 
        lh =self.isIdentical(r1.left,r2.left)
        rh =self.isIdentical(r1.right,r2.right)
        return lh and rh and r1.data == r2.data

def isBalancedTree(root):
    if root == None:
        return 0
    lh = isBalancedTree(root.left)
    rh = isBalancedTree(root.right)

    if lh==-1 or rh==-1 or abs(lh-rh)>1:
        return -1
    
    return max(lh,rh)+1

def checkBalancedTree(root):
    return True if isBalancedTree(root)>0 else False
    

def children_sum(root):
    def dfs(root):
        if not root:
            return True, 0
        if not root.left and not root.right:
            return True, root.key
        l_valid, left = dfs(root.left)
        r_valid, right = dfs(root.right)
        if l_valid and r_valid and (root.key == left+right):
            return True, root.key
        return False, 0
    
    val, _ = dfs(root)
    return val


def alt_childrenSum(root):
    # code 
    if root==None:
        return 0
    else:
        return 1 if dfs(root)==root.key else 0
        
def dfs(root):
    if root == None:
        return 0
        
    if root.left==None and root.right==None:
        return root.key
            
    lh = dfs(root.left)
    rh = dfs(root.right)
        
    return root.key if lh+rh==root.key else math.inf


root = Node(10)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(3)
root.right.left = Node(3)
root.right.right = Node(4)
 
print(alt_childrenSum(root))
