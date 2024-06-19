# 189
def rotate_array(nums: list[int], k: int) -> None:
    # O(1) memory
    k = k % len(nums)
    if not k:
        return

    left, right = 0, len(nums) - 1
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left, right = 0, k - 1
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left, right = k, len(nums) - 1
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
