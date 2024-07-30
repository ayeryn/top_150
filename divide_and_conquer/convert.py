# 108

from tree.TreeNode import TreeNode


def convert(nums: list[int]) -> TreeNode:
    def build(left, right):
        if left == right:
            return TreeNode(nums[left])

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        if left <= mid - 1:
            node.left = build(left, mid - 1)
        if mid + 1 <= right:
            node.right = build(mid + 1, right)
        return node

    return build(0, len(nums) - 1)
