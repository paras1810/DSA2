class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def isleaf(node):
    if node.left==None and node.right==None:
        return True 
    return False 

def left_traverse(node, res):
    node = node.left
    while node is not None:
        if isleaf(node) is not True:
            res.append(node.value)
        if node.left is not None:
            node = node.left
        else:
            node = node.right

def right_traverse(node, res):
    node = node.right
    stk = []
    while node is not None:
        if isleaf(node) is not True:
            stk.append(node.value)
        if node.right is not None:
            node = node.right
        else:
            node = node.left
    while(len(stk)!=0):
        res.append(stk.pop(-1))

def addleaves(root, res):
    if root is None:
        return 
    if isleaf(root) is True:
        res.append(root.value)
        return
    addleaves(root.left, res)
    addleaves(root.right, res)

def boundary(root, res):
    if root is None:
        return 
    if isleaf(root) is not True:
        res.append(root.value)
    left_traverse(root, res)
    addleaves(root, res)
    right_traverse(root, res)

if __name__=="__main__":
    root=Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)

    res = []
    boundary(root, res)
    print(res)
