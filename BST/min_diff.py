# 530

from tree.TreeNode import TreeNode


def min_diff(root: TreeNode) -> int:
    nodes = []

    def dfs(node):
        nonlocal nodes

        if not node:
            return

        dfs(node.left)
        nodes.append(node.val)
        dfs(node.right)

    dfs(root)  # put all values in an array (sorted)
    ans = float("inf")
    for i in range(1, len(nodes)):  # pass through the array
        ans = min(ans, nodes[i] - nodes[i - 1])
    return ans
