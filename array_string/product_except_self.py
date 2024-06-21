def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    left_cache = [1] * n  # product of nums[:i]
    right_cache = [1] * n  # product of nums[i+1:]

    for i in range(1, n):
        left_cache[i] = left_cache[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right_cache[i] = right_cache[i + 1] * nums[i + 1]

    for i in range(n):
        # Reuse num for return value
        nums[i] = left_cache[i] * right_cache[i]

    return nums
