from collections import defaultdict


# 169
def majority(nums: list[int]) -> int:
    count = 1
    ans = nums[0]

    for n in nums:
        if n == ans:
            count += 1
        else:
            count -= 1

            if count == -1:
                ans = n
                count = 0

    return ans


def majority_hash(nums: list[int]) -> int:
    d = defaultdict(int)

    for n in nums:
        d[n] += 1

        if d[n] >= (len(nums) + 1) // 2:
            return n


nums = [2, 2, 1, 1, 1, 2, 2]
print(majority(nums))
