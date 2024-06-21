# 45


def jump_greedy(nums):
    # TODO: implement

    pass


def jump_brute(nums: list[int]) -> int:
    n = len(nums)
    dp = [float("inf")] * n
    dp[0] = 0

    for i in range(n - 1):
        for j in range(i + 1, min(n, i + nums[i] + 1)):
            # Update reachable indexes from i
            dp[j] = min(dp[i] + 1, dp[j])
            if j == n - 1:
                # return if we reach the end early
                return dp[n - 1]

    return dp[-1]
