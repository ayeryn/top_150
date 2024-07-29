# 230

from tree.TreeNode import TreeNode


def kthSmallest(root: "TreeNode", k: int) -> int:
    def dfs(node, count):
        """
        Since we are dealing with BST, an inorder traversal returns nodes in sorted order

        Returns:
        - count: how many nodes visited
        - val: node.val or -1 if None
        """
        if not node:
            return count, -1

        l_count, l_val = dfs(node.left, count)
        if l_count == k:
            # target is in the left subtree
            return k, l_val
        if l_count + 1 == k:
            # target is node
            return k, node.val

        # target is in the right subtree
        r_count, r_val = dfs(node.right, l_count + 1)

        return r_count, r_val

    _, ret = dfs(root, 0)
    return ret
