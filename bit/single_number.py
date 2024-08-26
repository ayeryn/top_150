# 136


def single_number(nums: list[int]):
    ans = 0

    for n in nums:
        # self ^ self = 0
        # x ^ 0 = x
        ans ^= n

    return ans
