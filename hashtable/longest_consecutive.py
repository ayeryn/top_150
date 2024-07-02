def longestConsecutive(self, nums: list[int]) -> int:
    ans = 0
    n_set = set(nums)  # convert to set for O(1) membership check

    while n_set:
        x = n_set.pop()  # choose arbitrary item
        left = x - 1
        right = x + 1

        while left in n_set:  # find all consecutive smaller nums
            n_set.remove(left)
            left -= 1
        while right in n_set:  # find all consecutive larger nums
            n_set.remove(right)
            right += 1

        ans = max(ans, right - left - 1)  # update max

    return ans
