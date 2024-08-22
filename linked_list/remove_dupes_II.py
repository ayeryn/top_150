# 82

from typing import Optional
from ListNode import ListNode


def remove_dupes(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    prev = None
    curr = head
    while curr:
        after = curr.next
        count = 0
        while after and after.val == curr.val:
            # Check if curr has dupes
            count += 1
            after = after.next

        if count > 0:
            # there are duplicates of curr
            # after is pointing to the next element with different value
            if prev:
                # Remove dupes from linked list
                prev.next = after
            else:
                # head has dupe, update head and leave prev as None
                head = after
            curr = after
        else:
            # curr is unique, update variables
            prev = curr
            curr = curr.next

    return head
