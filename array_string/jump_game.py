# 55


def jump_game(nums: list[int]) -> bool:
    dp = [False] * len(nums)
    dp[0] = True

    for i in range(0, len(nums) - 1):  # O(n)
        # Note that if n[i] == True then all(n[0:i]) == True
        if dp[i]:
            if i + nums[i] >= len(nums) - 1:
                return True
            dp[i + 1 : i + nums[i] + 1] = [True] * nums[i]  # O(nums[i])
        else:
            # If False appears before endloop, we cannot reach any later indexes
            return False
    return dp[-1]
