# 11


def max_water(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    ans = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])
        ans = max(ans, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans
