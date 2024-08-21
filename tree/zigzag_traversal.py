#

from typing import Optional
from collections import deque
from TreeNode import TreeNode


def zigzag(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []

    ans = []
    tree = deque([root])
    l2r = True
    while tree:
        level = deque()
        nodes = len(tree)
        for _ in range(nodes):
            node = tree.popleft()
            if l2r:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                tree.append(node.left)
            if node.right:
                tree.append(node.right)
        ans.append(level)
        l2r = not l2r

    return ans
