# 242

from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    count = defaultdict(int)

    for c in s:
        count[c] += 1

    for c in t:
        count[c] -= 1
        if count[c] < 0:
            return False

    for k in count:
        if count[k] != 0:
            return False

    return True
