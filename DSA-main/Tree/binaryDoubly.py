class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

prev = None
def Binarydoubly(root):
    if root is None:
        return root
    head = Binarydoubly(root.left)
    global prev 
    if prev is None:
        head = root 
    else:
        root.left = prev 
        prev.right = root 
    prev = root 
    Binarydoubly(root.right)
    return head

def print_dll(root):
    while root is not None:
        print(root.value)
        root=root.right

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    
    head = Binarydoubly(root)
    print_dll(head)