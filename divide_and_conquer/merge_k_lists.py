# 23

from typing import Optional, List
from linked_list.ListNode import ListNode


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Brute-force: merge 2 lists together at a time
    if len(lists) == 0:
        return None

    def merge(l1, l2):
        # Merge 2 linked lists
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = None
        tail = None
        curr1 = l1
        curr2 = l2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                if not head:
                    head = curr1
                    tail = curr1
                    curr1 = curr1.next
                else:
                    temp = curr1
                    curr1 = curr1.next
                    tail.next = temp
                    tail = tail.next

            else:
                if not head:
                    head = curr2
                    tail = curr2
                else:
                    temp = curr2
                    curr2 = curr2.next
                    tail.next = temp
                    tail = tail.next

        if curr1:  # append rest of leftover
            tail.next = curr1
        if curr2:
            tail.next = curr2

        return head

    merged = None
    for l in lists:
        merged = merge(merged, l)
    return merged
