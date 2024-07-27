# 222

from typing import Optional
from collections import deque
from TreeNode import TreeNode


def count_nodes(root):
    # TODO: less than O(N) runtime
    pass


def count_nodes_n(root: Optional[TreeNode]) -> int:
    """
    Always terminate one level early
    Gets closer to O(N) as N grows larger
    """

    if not root:
        return 0

    tree = deque()
    tree.append(root)
    level = total = 0

    while tree:
        nodes = len(tree)
        count = 0
        for _ in range(nodes):
            node = tree.popleft()

            # Terminate early once we encounter a node with 0 or 1 child
            if not node.left:  # this is the last level
                # 2 ** level: all nodes on current level
                # (count * 2): nodes on this level that has children
                return total + 2**level + (count * 2)

            if node.left and not node.right:
                # 1: node.left
                return total + 2**level + (count * 2) + 1

            count += 1  # count current node

            # Would've terminated early if node doesn't have both children
            tree.append(node.left)
            tree.append(node.right)

        total += count
        level += 1

    return total
