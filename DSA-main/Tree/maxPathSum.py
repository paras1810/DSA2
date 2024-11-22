
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_max_sum(root):
    max_sum = float('-inf')
    st = []
    st.append((root, 0))
    if root is None:
        return 0
    while st:
        node, state = st.pop()
        if node is None:
            continue
        if state == 0:
            st.append((node, 1))
            st.append((node.left, 0))
        elif state == 1:
            st.append((node, 2))
            st.append((node.right, 0))
        else:
            left_sum = node.left.data if node.left is not None else 0
            right_sum = node.right.data if node.right is not None else 0
            max_sum = max(max_sum, (node.data+ max(0, left_sum)+ max(0, right_sum)))
            max_child_sum = max(left_sum, right_sum)
            node.data += max(0, max_child_sum)

    return max_sum


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(-25)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)

    max_sum = find_max_sum(root)
    print("Maximum Path Sum:", max_sum)