# 215

from heapq import heappush, heappop


def findKthLargest(nums: list[int], k: int) -> int:
    heap = []

    for n in nums:
        heappush(heap, -n)

    while k:
        top = -heappop(heap)
        k -= 1
        if k == 0:
            return top
