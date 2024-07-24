# 112

from typing import Optional
from TreeNode import TreeNode


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:  # no path sum
        return False

    def dfs(node, target):
        if (not node.left and not node.right) and target == node.val:
            # base case:
            # make sure node is leaf when returning True
            return True

        left = right = False
        # only perform recursion when child is not null per base case
        if node.left:
            left = dfs(node.left, target - node.val)

        if node.right:
            right = dfs(node.right, target - node.val)

        return left or right

    return dfs(root, targetSum)
