# 173

from TreeNode import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = [root]
        self.dfs()  # Traverse as we go

    def dfs(self):  # O(H)
        while self.stack[-1].left:
            # Get the leftmost path to get smallest element
            self.stack.append(self.stack[-1].left)

    def next(self) -> int:  # Avg. O(1)
        ret = self.stack.pop()
        if ret.right:
            # traverse down right child
            self.stack.append(ret.right)
            self.dfs()
        return ret.val

    def hasNext(self) -> bool:
        return len(self.stack) > 1
