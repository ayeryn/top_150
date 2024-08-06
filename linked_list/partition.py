# 86

from typing import Optional
from ListNode import ListNode


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    if not head:  # Empty list
        return head

    curr = head
    first = None
    while curr and curr.val < x:
        # Find the start of second partition
        first = curr
        curr = curr.next

    if not curr:
        # All elements are < x, no need to partition
        return head

    """
    - first < x, curr >= x
    - first is insertion point for first partition
    - curr is head of second partition
    - keep a copy of second_head for linking later
    """
    second_head, second = curr, curr
    curr = curr.next

    while curr:
        # Move elements to the front if curr.val < x
        if curr.val < x:
            if first:  # There are elements in the first partition
                first.next = curr
                first = curr
            else:
                # Empty first partition
                # curr becomes head
                head = curr
                first = head
            second.next = curr.next
        else:
            # Move second
            second = second.next

        curr = curr.next

    # Link first and second partitions
    if first:
        first.next = second_head
        return head
    else:
        # Empty first partition, second_head is head
        return second_head
