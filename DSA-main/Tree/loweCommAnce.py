class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if not root or root==p or root==q:
        return root
    left_lca = lowest_common_ancestor(root.left, p, q)
    right_rca = lowest_common_ancestor(root.right, p, q)
    if left_lca and right_rca:
        return root
    return left_lca if left_lca else right_rca


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)

    p = root.left
    q = root.left.right

    lca1 = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is {lca1.val}")

    x = root.right.right
    y = root.right.right.right

    lca2 = lowest_common_ancestor(root, x, y)
    print(f"LCA of {x.val} and {y.val} is {lca2.val}")