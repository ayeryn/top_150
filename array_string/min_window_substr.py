# 76
from collections import defaultdict


def min_window_substr_brute(s: str, t: str) -> str:
    if s == t:
        return s
    if len(s) < len(t):
        return ""

    ans = ""
    left = 0
    count = defaultdict(int)
    for c in t:
        count[c] += 1
    d = defaultdict(int)

    def is_ans():
        return all([count[key] <= d[key] for key in count])

    for right in range(len(s)):
        if s[right] in count:
            d[s[right]] += 1

        while is_ans():
            if ans == "" or len(ans) > (right - left + 1):
                ans = s[left : right + 1]
            if s[left] in count:
                d[s[left]] -= 1
            left += 1

    return ans
