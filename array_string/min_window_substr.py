# 76
from collections import defaultdict


def min_window_substr(s: str, t: str) -> str:
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

    for right in range(len(s)):
        if s[right] in count:
            d[s[right]] += 1

        while count == d:
            # FIXME: count of a char c might exceed count[c]
            if ans == "" or len(ans) > (right - left + 1):
                ans = s[left : right + 1]
            if s[left] in count:
                d[s[left]] -= 1
            left += 1

        while s[right] in count and d[s[right]] > count[s[right]]:
            # FIXME: incorrectly shortens substr
            if s[left] in count:
                d[s[left]] -= 1
            left += 1

    return ans
