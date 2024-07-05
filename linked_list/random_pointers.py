# 138
from ListNode import ListNode as Node
from typing import Optional


def copyRandomList(head: "Optional[Node]") -> "Optional[Node]":
    copy = Node(0)
    copy_pt = copy
    head_pt = head

    # map original to its deep copy
    # ensures we don't copy the same node twice
    mapping = {}

    while head_pt:
        if head_pt not in mapping:
            # Create new node only when we haven't by pointing randoms
            copy_pt.next = Node(head_pt.val)
            mapping[head_pt] = copy_pt.next  # update mapping
        else:
            copy_pt.next = mapping[head_pt]

        if head_pt.random:
            # same logic for random pointers
            if head_pt.random not in mapping:
                copy_pt.next.random = Node(head_pt.random.val)
                mapping[head_pt.random] = copy_pt.next.random
            else:
                copy_pt.next.random = mapping[head_pt.random]

        head_pt = head_pt.next
        copy_pt = copy_pt.next

    return copy.next
