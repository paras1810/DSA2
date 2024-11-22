class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

s = set()
st = []

def buildTree(preorder, inorder, n):
    root = None
    pre = 0
    in_t = 0
    while pre < n:
        node = None
        while True:
            node = TreeNode(preorder[pre])
            if root == None:
                root = node

            if len(st) > 0:
                if st[-1] in s:
                    s.discard(st[-1])
                    st[-1].right = node
                    st.pop()
                else:
                    st[-1].left = node
            st.append(node)

            if pre>=n or preorder[pre]==inorder[in_t]:
                pre+=1
                break
            pre+=1
        node =None

        while len(st)>0 and in_t<n and st[-1].val==inorder[in_t]:
            node = st[-1]
            st.pop()
            in_t+=1

        if node != None:
            s.add(node)
            st.append(node)
    return root

def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=' ')
    printInorder(root.right)

if __name__ =='__main__':

    in_t = [ 9, 8, 4, 2, 10, 5, 10, 1, 6, 3, 13, 12, 7 ]
    pre = [ 1, 2, 4, 8, 9, 5, 10, 10, 3, 6, 7, 12, 13 ]
    l = len(in_t)

    root = buildTree(pre, in_t, l);

    printInorder(root);