def summary_ranges(self, nums: list[int]) -> list[str]:
    ans = []
    i = 0

    while i < len(nums):
        start = i
        while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1

        if start == i:
            ans.append(str(nums[start]))
        else:
            ans.append(f"{nums[start]}->{nums[i]}")
        i += 1
    return ans
