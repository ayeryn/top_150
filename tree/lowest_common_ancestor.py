# 236

from TreeNode import TreeNode


def LCA(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    def dfs(node):
        if not node:
            return

        """
        2 scenarios:
        1. diff tree
        2. same tree - whichever comes first
        """
        if node.val == p.val or node.val == q.val:
            # return once we find p or q
            return node

        left = dfs(node.left)
        right = dfs(node.right)

        # same subtree
        if left and not right:
            return left
        if right and not left:
            return right

        if left and right:
            # different subtree, node is LCA
            return node

        return dfs(root)
