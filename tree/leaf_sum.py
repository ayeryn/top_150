# 129

from TreeNode import TreeNode


def leaf_sum(root: TreeNode) -> int:
    def dfs(node, num):
        # num is current number formed along the path
        if not node:
            # nothing to add to sum
            return 0

        if not node.left and not node.right:
            # terminate at leaf
            return num * 10 + node.val

        left = dfs(node.left, num * 10 + node.val)
        right = dfs(node.right, num * 10 + node.val)
        return left + right

    return dfs(root, 0)
