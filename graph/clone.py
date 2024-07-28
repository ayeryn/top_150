# 133


from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone(node: Optional["Node"]) -> Optional["Node"]:
    # Map original node to its copy
    mapping = {}

    def dfs(node):
        """
        1. Creates copy of node
        2. Appends neighbors of node to its copy
        """
        nonlocal mapping
        if not node:
            return None

        if node not in mapping:
            # Create copy if it doesn't exist
            mapping[node] = Node(node.val)
        copy = mapping[node]

        for n in node.neighbors:
            n_copy = mapping[n] if n in mapping else dfs(n)
            copy.neighbors.append(n_copy)
        return copy

    return dfs(node)
