# 55
def jump_game_brute(nums: list[int]) -> bool:
    n = len(nums)
    reach = [False] * n
    reach[0] = True

    # Find all reachable indexes
    # Exclude last index as it's the destination
    for i in range(n - 1):
        if reach[i]:
            for j in range(1, nums[i] + 1):  # This could be super large
                reach[min(i + j, n - 1)] = True

    return reach[-1]
