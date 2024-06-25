def three_sum_2p(nums):  # O(n^2)
    ans = set()
    nums.sort()  # In order to optimize for x and use 2p for y,z
    if nums[-1] < 0:
        return ans

    x = 0
    while x < len(nums) and nums[x] <= 0:
        # x has to be <=0 if 3sum == 0
        # solve for x and y using 2 pointers
        target = -nums[x]
        y, z = x + 1, len(nums) - 1
        while y < z:
            total = nums[y] + nums[z]
            if total == target:
                ans.add((nums[x], nums[y], nums[z]))
            if total > target:
                z -= 1
            else:
                y += 1
        x += 1
    return ans


def three_sum_brute(nums):  # O(n^3)
    ans = set()
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            for z in range(y + 1, len(nums)):
                if nums[x] + nums[y] + nums[z] == 0:
                    ans.add((nums[x], nums[y], nums[z]))
    return ans
