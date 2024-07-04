# 141
from ListNode import ListNode
from typing import Optional


def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head:
        return False

    seen = set()
    while head:
        if head not in seen:
            seen.add(head)
            head = head.next
        else:
            return True
    return False
