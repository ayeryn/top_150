# 300


def LIS(nums: list[int]):
    if len(nums) == 1:
        return 1

    ans = 1
    dp = [1 for _ in range(len(nums))]
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
        ans = max(ans, dp[i])

    return ans


def LIS_2D(nums: list[int]) -> int:
    def dp(i, seq):
        if i == len(nums):
            return len(seq)

        if not seq or nums[i] > seq[-1]:
            return dp(i + 1, seq + [nums[i]])
        else:  # num is smaller than curr seq[-1]
            new_seq = [n for n in seq if n < nums[i]]
            new_seq.append(nums[i])
            cont = dp(i + 1, new_seq)
            restart = dp(i + 1, [nums[i]])
            skip = dp(i + 1, seq)
            return max(cont, restart, skip)

    return dp(0, [])


def LIS_mono_stack(nums):
    """
    Monotonic stack will NOT work
    E.g.: [0,1,0,3,2,3]
    Once it reaches the second 0, it will empty the stack and get rid of "1",
    which should be in the LIS
    """
    stack = []
    ans = 1

    for i in range(len(nums)):
        while stack and stack[-1] >= nums[i]:
            ans = max(ans, len(stack))
            stack.pop()
        stack.append(nums[i])
    ans = max(ans, len(stack))

    return ans
