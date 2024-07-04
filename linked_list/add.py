# 2
from ListNode import ListNode
from typing import Optional


def add(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    tenth = 0
    ans = ListNode(0)
    node = ans

    while l1 and l2:
        res = l1.val + l2.val + tenth
        node.next = ListNode(res % 10)
        tenth = res // 10
        l1 = l1.next
        l2 = l2.next
        node = node.next

    while l1:
        res = l1.val + tenth
        node.next = ListNode(res % 10)
        tenth = res // 10
        node = node.next
        l1 = l1.next

    while l2:
        res = l2.val + tenth
        node.next = ListNode(res % 10)
        tenth = res // 10
        node = node.next
        l2 = l2.next

    if tenth:
        node.next = ListNode(1)

    return ans.next
