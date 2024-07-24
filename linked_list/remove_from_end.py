# 19

from typing import Optional
from ListNode import ListNode


def remove_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    nodes = []  # construct array from linked list
    curr = head

    while curr:
        nodes.append(curr)
        curr = curr.next

    ind = -n

    # remove head
    if nodes[ind] == head:
        return head.next if len(nodes) > 1 else None

    if n == 1:
        nodes[ind - 1].next = None
    else:
        nodes[ind - 1].next = nodes[ind + 1]
    return head
