# 105

from TreeNode import TreeNode
from collections import defaultdict


"""
preorder: node -> left -> right
inorder : left -> node -> right
"""


def construct_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    if len(preorder) == 1:  # one-node tree
        return TreeNode(preorder[0])

    """
    1. root = p[0]
    2. everything before root in inorder is root.LHS
    3. everything after root in inorder is root.RHS
    4. if inorder[0] != root then inorder[0] is the leftmost leaf
    """
    root = TreeNode(preorder[0])
    val_node = defaultdict(TreeNode)
    val_node[root.val] = root
    curr = root
    p_i = i_i = 0

    def build(pi, ii, curr):
        nonlocal val_node
        while pi < len(preorder) and preorder[pi] != inorder[ii]:
            # find all LHS nodes
            curr.left = TreeNode(preorder[pi])
            pi += 1
            curr = curr.left
            val_node[curr.val] = curr

        if pi == len(preorder):
            return -1, -1

        curr.left = TreeNode(preorder[pi])
        curr = curr.left
        val_node[curr.val] = curr
        pi += 1
        ii += 1
        while ii < len(inorder) and inorder[ii] != root.val:
            if inorder[ii] not in val_node:
                parent = val_node[inorder[ii - 1]]
                parent.right = TreeNode(inorder[ii])
                val_node[parent.right.val] = parent.right
            ii += 1

        if ii == len(inorder) - 1:
            return -1, -1
        ii += 1

        while pi < len(preorder) and preorder[pi] in val_node:
            # skip all processed nodes
            pi += 1
        return pi, ii

    """ LHS """
    if inorder[0] != root.val:  # LHS not empty
        # build LHS
        p_i, i_i = build(1, 0, curr)
        if p_i == -1:
            return root
    else:
        p_i = 1
        i_i = 1

    """ RHS """
    root.right = TreeNode(preorder[p_i])
    val_node[preorder[p_i]] = root.right
    curr = root.right
    p_i += 1

    if p_i == len(preorder):
        return root

    # build RHS
    build(p_i, i_i, curr)

    return root
