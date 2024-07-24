# 105
# divide and conquer
# Check out easy 108

from TreeNode import TreeNode
from collections import defaultdict


"""
preorder: node -> left -> right
inorder : left -> node -> right
"""


def construct_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    in_index = {}
    for i in range(len(inorder)):
        in_index[inorder[i]] = i

    pi = 0

    def build(left, right):
        # we are building in preorder => increase pi at each step
        nonlocal pi
        if pi >= len(preorder):  # terminate
            return None

        if left == right:  # reached leaf
            leaf = TreeNode(preorder[pi])
            pi += 1
            return leaf

        root = TreeNode(preorder[pi])
        pi += 1
        ind = in_index[root.val]

        # only make children if they exist (valid left-right range)
        if left <= ind - 1:
            root.left = build(left, ind - 1)

        if ind + 1 <= right:
            root.right = build(ind + 1, right)
        return root

    return build(0, len(preorder) - 1)
