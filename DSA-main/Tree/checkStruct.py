class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSameStructure(root1, root2):
    if root1 == None and root2 == None:
        return 1
    if root1 != None and root2 != None:
        return isSameStructure(root1.left, root2.left) and isSameStructure(root1.right, root2.right)
    return 0

if __name__ =='__main__':

    root1 = newNode(10);
    root2 = newNode(100);
    root1.left = newNode(7);
    root1.right = newNode(15);
    root1.left.left = newNode(4);
    root1.left.right = newNode(9);
    root1.right.right = newNode(20);

    root2.left = newNode(70);
    root2.right = newNode(150);
    root2.left.left = newNode(40);
    root2.left.right = newNode(90);
    root2.right.right = newNode(200);

    if (isSameStructure(root1, root2)):
        print("Both trees have same structure");
    else:
        print("Trees do not have same structure");