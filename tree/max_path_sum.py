# 124


from functools import cache
from TreeNode import TreeNode


def max_path_sum(root: "TreeNode") -> int:
    @cache
    def dfs(node):
        """
        Returns: (int, int) indicating split_sum and nosplit_sum

        - split_sum: max path sum if split at root. can no longer split further up the tree.
        - nosplit_sum: max path sum if didn't split down the root, can split further up the tree.
        """
        nonlocal ret
        if not node:
            return float("-inf"), float("-inf")

        left_s, left_nos = dfs(node.left)
        right_s, right_nos = dfs(node.right)

        # Split 1: split at node, no split down the children
        s = left_nos + right_nos + node.val

        # Split 2: no split at node, split at children
        s = max(s, max(left_s, right_s))

        # No_split 1: No split at root, no split at children - choose one path
        nos = max(left_nos, right_nos) + node.val

        # No_split 2: start path at node
        nos = max(nos, node.val)

        ret = max(ret, s, nos)
        return s, nos

    # Keep track of max
    # A single node is considered a path
    ret = root.val
    dfs(root)
    return ret
