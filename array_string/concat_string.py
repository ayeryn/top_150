# 30
from collections import defaultdict


def concat_string(s: str, words: list[str]) -> list[int]:
    ans = []
    w = len(words[0])
    n = w * len(words)
    count = defaultdict(int)  # counter hashmap for words
    for word in words:
        count[word] += 1

    for right in range(len(s) - n + 1):
        # TODO: optimize with has variable??
        if s[right : right + w] not in count:
            continue

        curr = s[right : right + n]  # grab possible substring and do checks
        d = defaultdict(int)  # counter for substring
        for i in range(0, len(curr), w):
            d[curr[i : i + w]] += 1
        if d == count:  # found a solution
            ans.append(right)

    return ans
