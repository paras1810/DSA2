# Flip binary tree towards right direction i.e clockwise
# root->left->left = root->right
# root->left->right = root
# root->left = NULL
# root->right = NULL 


import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def flipBinaryTree(root):
    if root is None:
        return root

    if root.left is None and root.right is None:
        return root

    flippedRoot = flipBinaryTree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None
    return flippedRoot



def printLevelOrder(root):
    if root is None:
        return
    q = queue.Queue(maxsize=6)
    q.put(root)

    while True:
        nodeCount = q.qsize()
        if nodeCount == 0:
            break
        while nodeCount > 0:
            node = q.get()
            print(node.data, end=" ")
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            nodeCount -= 1
        print()



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    printLevelOrder(root)

    root = flipBinaryTree(root)
    printLevelOrder(root)