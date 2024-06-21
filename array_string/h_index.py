def h_index(citations: list[int]) -> int:
    citations.sort()
    ans = left = 0
    # print(citations)

    for right in range(len(citations)):
        if citations[right] == 0:
            # skip all 0's
            left += 1
            continue

        """ Sliding Window
        - len(window) >= ans
        - citations[left] >= ans
        """
        # print(f"w = {citations[left:right+1]}, ans = {ans}")
        if (right + 1 - left) <= citations[left]:
            # if len(window) <= min citations in the window
            # increase h-index
            ans += 1
            # print(f"Update ans -> {ans}")
        else:
            # update window
            left += 1
            # print(f"Update window")

    return ans


c = [3, 0, 6, 1, 5]
print(h_index(c))
