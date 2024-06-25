# 3
from collections import defaultdict


def longest_seq(s: str) -> int:
    count = defaultdict(int)
    left = ans = 0

    for right in range(len(s)):
        count[s[right]] += 1

        while count[s[right]] > 1:
            count[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans
