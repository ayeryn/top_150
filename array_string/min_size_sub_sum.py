# 209


def min_size_sub_sum(nums: list[int], target: int) -> int:
    left = total = 0
    ans = float("inf")

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:  # update window and get all solutions
            ans = min(ans, right - left + 1)
            total -= nums[left]
            left += 1

    return ans if ans != float("inf") else 0
