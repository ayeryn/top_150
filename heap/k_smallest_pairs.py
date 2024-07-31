# 373

from heapq import heappop, heappush


def find_pairs(nums1, nums2, k):
    heap = []
    ans = []

    # Use a heap to track the smallest possible sum for each x
    for i in range(len(nums1)):
        heappush(heap, (nums1[i] + nums2[0], i, 0))

    while i < len(nums1) and k:
        top = heappop(heap)
        i, j = top[1], top[2]
        ans.append([nums1[i], nums2[j]])
        j += 1
        k -= 1

        while (
            j < len(nums2)
            and (heap and nums1[i] + nums2[j] < heap[0][0] or not heap)
            and k
        ):
            ans.append([nums1[i], nums2[j]])
            j += 1
            k -= 1

        if j < len(nums2):
            # Update heap
            heappush(heap, (nums1[i] + nums2[j], i, j))

    return ans


def find_pairs_brute(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    heap = []

    # Brute force, not using the non-decreasing property of nums arrays
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            heappush(heap, (nums1[i] + nums2[j], i, j))

    ret = []
    print(heap)
    while k:
        top = heappop(heap)
        ret.append([top[1], top[2]])
        k -= 1
    return ret


n1 = [1, 1, 2]
n2 = [1, 2, 3]
find_pairs_brute(n1, n2, 2)
