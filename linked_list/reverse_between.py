# 92

from ListNode import ListNode
from typing import Optional


def reverseBetween(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    if left == right:
        return head

    count = 1
    prev = None
    node = head

    while node and count < left:
        # skip until segment and preserve prev to start of seg
        prev = node
        node = node.next
        count += 1

    next = node.next  # set next
    start = node  # set pointer to start of segment
    o_next = next.next if next else None  # set original next.next
    node.next = None  # reset node.next

    while node and count < right:
        next.next = node

        # move pt forward
        node = next
        next = o_next
        if o_next:
            o_next = o_next.next
        count += 1

    # link segment back into list
    if prev:
        prev.next.next = next
        prev.next = node
        return head
    else:
        start.next = next
        return node
