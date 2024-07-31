#

from functools import cache


def rob(nums: list[int]) -> int:
    @cache
    def dp(i):
        if i >= len(nums):
            return 0

        rob = nums[i] + dp(i + 2)
        skip = dp(i + 1)
        return max(rob, skip)

    return dp(0)
