# 53
# Kadane's Algorithm


def max_subarray(nums: list[int]) -> int:
    curr_sum = ans = nums[0]

    for i in range(1, len(nums)):
        # curr_sum is the sum of all prev valid subarray
        if curr_sum < 0:
            # Chop off negative "prefix"
            curr_sum = nums[i]
        else:
            # Positive sequence - add current number
            curr_sum += nums[i]
        ans = max(ans, curr_sum)

    return ans
