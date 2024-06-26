# 76
from collections import defaultdict


def min_window_substr(s: str, t: str) -> str:  # O(M+N)
    # M - len(s), N = len(t)
    if s == t:
        return s
    if len(s) < len(t):
        return ""

    ans = ""
    left = 0
    count = defaultdict(int)
    for c in t:  # O(N)
        count[c] += 1
    d = defaultdict(int)
    has = 0  # keep track of how many chars in t we have found

    for right in range(len(s)):  # O(M)
        if s[right] in count:
            d[s[right]] += 1
            has += d[s[right]] <= count[s[right]]  # update has

        while has == len(t):  # we have found a solution
            if ans == "" or len(ans) > (right - left + 1):
                ans = s[left : right + 1]
            if s[left] in count:
                d[s[left]] -= 1
                has -= d[s[left]] < count[s[left]]  # update has
            left += 1

    return ans
