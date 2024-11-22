class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, x):
    if root == None:
        return Node(x)
    if x<root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right,x)
    return root

def kthsmall(root):
    global k
    if root == None:
        return None
    left = kthsmall(root.left)
    if left != None:
        return left
    k -= 1
    if k == 0:
        return root
    return kthsmall(root.right)

def printKthSmallest(root):
    res = kthsmall(root)
    if res == None:
        print("Less than k nodes in Tree")
    else:
        print("Kth small element is", res.data)
if __name__ == '__main__':

    root = None
    keys = [20, 8, 22, 4, 12, 10, 14]

    for x in keys:
        root = insert(root, x)

    k = 3

    printKthSmallest(root)