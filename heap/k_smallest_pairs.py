# 373

from heapq import heappop, heappush


def find_pairs(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    heap = []

    # Brute force, not using the non-decreasing property of nums arrays
    for x in nums1:
        for y in nums2:
            heappush(heap, (x + y, x, y))

    ret = []
    while k:
        top = heappop(heap)
        ret.append([top[1], top[2]])
        k -= 1
    return ret
