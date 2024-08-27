# 23

from typing import Optional, List
from heapq import *
from linked_list.ListNode import ListNode


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


def merge_k_lists(lists):  # O(ologk)
    if len(lists) == 0:
        return None

    while len(lists) > 1:
        # We will still touch the elements more than once but logk
        temp = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            temp.append(merge(l1, l2))

        lists = temp

    return lists[0]


def merge_k_lists_heap(lists):
    # This does not use the sorted linked list property
    # Also uses extra memory because it's creating new nodes
    # Kind of cheating with heap's sorting property
    if len(lists) == 0:
        return None

    heap = []
    for l in lists:
        # Push all values onto heap
        curr = l
        while curr:
            heappush(heap, curr.val)
            curr = curr.next

    head = None
    tail = None
    while heap:
        top = heappop(heap)

        if not head:
            head = ListNode(top)
            tail = head
        else:
            tail.next = ListNode(top)
            tail = tail.next

    return head


def merge_k_lists_brute(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Brute-force: merge 2 lists together at a time
    # This is slow because we are checking almost all elements more than onces
    if len(lists) == 0:
        return None

    merged = None
    for l in lists:
        merged = merge(merged, l)
    return merged
