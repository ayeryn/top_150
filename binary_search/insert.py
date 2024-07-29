# 35


def insert(nums: list[int], target: int) -> int:
    # We might insert after last element
    left, right = 0, len(nums)

    while left < right:
        # left == right when we found insert position
        mid = (left + right) // 2
        if nums[mid] == target:
            # target in num -> return position
            return mid

        if nums[mid] > target:
            # search left
            # we might insert at mid
            right = mid

        else:
            # search right
            # we wll always insert after mid
            left = mid + 1

    return left
