# 114

from typing import Optional
from TreeNode import TreeNode


def flatten(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root or (not root.left and not root.right):
        # base case, no need to process
        return

    nodes = []

    def dfs(node):
        nonlocal nodes
        if not node:
            return

        nodes.append(node)
        dfs(node.left)
        dfs(node.right)

    dfs(root)  # construct pre-order node array

    curr = root
    for i in range(1, len(nodes)):
        curr.left = None  # nullify left
        curr.right = nodes[i]
        curr = curr.right  # update curr
