def trap_water(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    ml, mr = height[0], height[-1]  # track max on each side
    ans = 0

    while left <= right:
        m_lr = min(ml, mr)  # bottleneck is the shorter edge

        # Calculate trapped water at index before moving pointers
        if ml < mr:
            area = m_lr - height[left]
            if area > 0:
                ans += area
            left += 1
        else:
            area = m_lr - height[right]
            if area > 0:
                ans += area
            right -= 1

        # Update max edges
        ml = max(ml, height[left])
        mr = max(mr, height[right])

    return ans
