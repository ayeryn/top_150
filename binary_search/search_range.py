# 34


def search_range(nums: list[int], target: int) -> list[int]:
    # TODO: Optimize and solve in single pass
    if len(nums) == 0:
        return [-1, -1]

    def search_start():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0:
                    return mid
                if mid - 1 >= 0 and nums[mid - 1] != target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search_end():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    return mid
                if mid + 1 < len(nums) and nums[mid + 1] != target:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    start = search_start()
    end = search_end()
    return [start, end]
