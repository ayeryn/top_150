# 199

from TreeNode import TreeNode
from typing import Optional
from collections import deque


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    ans = []
    tree = deque([root])

    while tree:
        nodes = len(tree)
        for _ in range(nodes - 1):
            curr = tree.popleft()
            if curr.left:
                tree.append(curr.left)
            if curr.right:
                tree.append(curr.right)

        right = tree.popleft()
        ans.append(right.val)
        if right.left:
            tree.append(right.left)
        if right.right:
            tree.append(right.right)

    return ans
