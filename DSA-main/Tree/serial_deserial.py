class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def serialize(self, root):
        if not root:
            return None
        st = [root]
        l = []
        while st:
            t = st.pop()
            if not t:
                l.append("#")
            else:
                l.append(str(t.data))
                st.append(t.right)
                st.append(t.left)
        return ','.join(l)

    def deserialize(self, data):
        if not data:
            return None
        global t
        t = 0
        arr = data.split(",")
        return self.helper(arr)

    def helper(self, arr):
        global t
        if arr[t] == "#":
            return None
        root = TreeNode(int(arr[t]))
        t += 1
        root.left = self.helper(arr)
        t += 1
        root.right = self.helper(arr)
        return root



    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
if __name__ == '__main__':
    # Construct a tree shown in the above figure
    tree = BinaryTree()
    tree.root = TreeNode(20)
    tree.root.left = TreeNode(8)
    tree.root.right = TreeNode(22)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(12)
    tree.root.left.right.left = TreeNode(10)
    tree.root.left.right.right = TreeNode(14)

    serialized = tree.serialize(tree.root)
    print("Serialized view of the tree:")
    print(serialized)
    print()

    # Deserialize the stored tree into root1
    t = tree.deserialize(serialized)

    print("Inorder Traversal of the tree constructed from serialized String:")
    tree.inorder(t)