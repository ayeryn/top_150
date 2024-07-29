# 46


def permute(nums: list[int]) -> list[list[int]]:

    def solve(curr, seen):
        if len(curr) == len(nums):
            # terminate when we reach desired length
            ans.append(curr[:])

        for ind in range(len(nums)):
            if nums[ind] not in seen:
                seen.add(nums[ind])
                curr.append(nums[ind])
                solve(curr, seen)
                curr.pop()
                seen.remove(nums[ind])

    ans = []
    for n in nums:
        solve([n], set([n]))

    return ans
