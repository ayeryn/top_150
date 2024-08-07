# 98

from tree.TreeNode import TreeNode


def validate(root: TreeNode) -> bool:

    def dfs(node):
        # TODO: Optimize for better runtime
        left = right = True
        lmax = rmin = node.val

        """
        For node to be a valid BST:
        1. left subtree is valid
        2. right subtree is valid
        3. max value in left subtree < node.val
        4. min value in right subtree > node.val
        """

        if node.left:
            if node.left.val >= node.val:
                left = False

            l_lmax, l_rmin, left = dfs(node.left)
            if l_lmax >= node.val:
                left = False

            lmax = max(lmax, rmin, l_lmax, l_rmin)
            rmin = min(lmax, rmin, l_lmax, l_rmin)

        if node.right:
            if node.right.val <= node.val:
                right = False

            r_lmax, r_rmin, right = dfs(node.right)
            if r_rmin <= node.val:
                right = False

            lmax = max(lmax, rmin, r_lmax, r_rmin)
            rmin = min(lmax, rmin, r_lmax, r_rmin)

        # Get max and min value of current subtree
        return max(lmax, rmin), min(lmax, rmin), left and right

    return dfs(root)[2]
