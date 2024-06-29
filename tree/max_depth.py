# 104
from TreeNode import TreeNode


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1
