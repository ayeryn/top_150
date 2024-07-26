# 236

from TreeNode import TreeNode


def LCA(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    if not root:
        return

    """
    2 scenarios:
    1. diff tree
    2. same tree - whichever comes first (by nature of recursion)
    """
    if root.val == p.val or root.val == q.val:
        # return once we find p or q
        return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    # same subtree
    if left and not right:
        return left
    if right and not left:
        return right

    if left and right:
        # different subtree, root is LCA
        return root
