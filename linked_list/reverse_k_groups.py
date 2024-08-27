#

from ListNode import ListNode


def reverse_k_groups(head: "ListNode", k: int) -> "ListNode":
    nodes = 0
    curr = head

    while curr:
        # Count nodes
        nodes += 1
        curr = curr.next

    if nodes == 1:
        return head  # Single node -> no operation needed

    prev = None
    curr = head
    while nodes >= k:
        tail = curr  # Keep track of new_tail
        pp = None
        next = None
        for i in range(k):
            # Reverse segment
            next = curr.next
            curr.next = pp
            pp = curr
            curr = next

        # Link reversed segment back into the list
        # tail -> new_Tail
        # pp -> new_head
        # curr -> start of next segment
        if prev is None:
            # First segment, update head
            head = pp
        else:  # Link with previous segment
            prev.next = pp
        prev = tail

        # Update nodes to reverse
        nodes -= k

    # Link reversed segments with leftover if any
    if nodes > 0:
        prev.next = curr

    return head
