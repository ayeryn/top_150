# 117

from collections import deque
from typing import Optional
from TreeNode import TreeNode


def populate_next(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root

    tree = deque()  # use BFS because we process by level
    tree.append(root)

    while tree:
        nodes = len(tree)
        prev = None  # keep track of the previous node

        for _ in range(nodes):
            node = tree.popleft()
            if prev:  # set prev.next to current node
                prev.next = node
            if node.left:
                tree.append(node.left)
            if node.right:
                tree.append(node.right)
            prev = node  # update prev
    return root
