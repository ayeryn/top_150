# 373

from heapq import heappop, heappush


def find_pairs(nums1, nums2):
    heap = []
    i = j = 0
    if len(nums1) > 1:
        next_i_sum = nums1[1] + nums2[j]
    else:
        next_i_sum = nums1[i] + nums2[j]

    while len(heap) < k and i < len(nums1):
        curr_sum = nums1[i] + nums2[j]
        print(
            f"next_sum = {next_i_sum}, i = {i}, x = {nums1[i]}, j = {j}, y = {nums2[j]}"
        )
        if j < len(nums2) and curr_sum < next_i_sum:
            print("Traverse nums2 ----")
            heappush(heap, [nums1[i], nums2[j]])
            print(f"x + y = {nums1[i] + nums2[j]}, {heap}")
            j += 1
        else:
            # Reached end of nums2 OR
            # n1[i] + n2[j] > n1[i+1] + n2[0]
            i += 1
            j = 0
            print(f"Increase i => {i}, restart nums2 => {j}")
            if i + 1 < len(nums1):
                next_i_sum = nums1[i + 1] + nums2[j]
                print("Update sum ", next_i_sum)

            print("\n")

    return heap


def find_pairs_brute(nums1: list[int], nums2: list[int]) -> list[list[int]]:
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
