# 106

from TreeNode import TreeNode


"""
preorder : node -> left -> right
inorder  : left -> node -> right
postorder: left -> right -> node

The key difference between this vs construct_tree is that:
1. postorder[-1] is root
2. Think about postorder in reverse => node -> right -> left
"""


def construct_tree(inorder: list[int], postorder: list[int]) -> TreeNode:
    if len(inorder) == 1:
        return TreeNode(inorder[0])

    in_index = {}
    for i in range(len(inorder)):
        in_index[inorder[i]] = i

    # reverse logic of preorder processing
    # start from end and progress node -> right -> left
    pi = len(postorder) - 1

    def build(left, right):
        nonlocal pi
        if pi < 0:
            return None

        if left == right:
            leaf = TreeNode(postorder[pi])
            pi -= 1
            return leaf

        root = TreeNode(postorder[pi])
        pi -= 1
        root_ind = in_index[root.val]

        if root_ind + 1 <= right:
            root.right = build(root_ind + 1, right)
        if left <= root_ind - 1:
            root.left = build(left, root_ind - 1)

        return root

    return build(0, len(inorder) - 1)
