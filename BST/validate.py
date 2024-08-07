# 98

from tree.TreeNode import TreeNode


def validate(root: TreeNode) -> bool:

    def dfs(node):
        # TODO: Optimize for better runtime
        left = right = True
        lmax = rmin = node.val

        if node.left:
            if node.left.val >= node.val:
                left = False
            llmax, llmin, left = dfs(node.left)
            if llmax >= node.val:
                left = False
            lmax = max(llmax, lmax, rmin, llmin)
            rmin = min(llmax, lmax, rmin, llmin)

        if node.right:
            if node.right.val <= node.val:
                right = False
            rlmax, rrmin, right = dfs(node.right)
            if rrmin <= node.val:
                right = False
            lmax = max(rlmax, lmax, rmin, rrmin)
            rmin = min(rlmax, lmax, rmin, rrmin)

        return max(lmax, rmin), min(lmax, rmin), left and right

    return dfs(root)[2]
