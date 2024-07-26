# 173

from TreeNode import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = []
        curr = self.root
        self.dfs(curr)
        self.next_ind = -1

    def dfs(self, node):  # O(N)
        if not node:
            return

        self.dfs(node.left)
        self.nodes.append(node.val)
        self.dfs(node.right)

    def next(self) -> int:
        self.next_ind += 1
        return self.nodes[self.next_ind]

    def hasNext(self) -> bool:
        return self.next_ind < len(self.nodes) - 1
