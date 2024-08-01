# 61

from typing import Optional
from ListNode import ListNode


def rotate(head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
    if k == 0 or not head:
        return head

    nodes = []
    curr = head
    while curr:
        # Put nodes into an array
        nodes.append(curr)
        curr = curr.next

    # Get number of rotations
    k %= len(nodes)
    if k == 0:
        return head

    # Unlink prev with new head
    nodes[-(k + 1)].next = None
    # Link tail with head
    nodes[-1].next = head

    return nodes[-k]
