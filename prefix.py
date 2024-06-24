def prefix_brute(strs: list[str]) -> str:
    # the longest prefix is determined by the shortest word
    # use strs[0] as reference point
    pre = strs[0]
    pi = min(len(w) for w in strs)

    while pi > 0:  # start with max possible index and go down
        f = False
        for i in range(1, len(strs)):
            if strs[i][:pi] != pre[:pi]:
                pi -= 1
                f = True
                break
        if not f:  # return if all words match the prefix
            return pre[:pi]

    return pre[:pi]


def prefix(strs):
    word = strs[0]
    ans = ""
    for i in range(len(word)):
        for s in strs:
            # Deal with length in the loop
            if len(s) == i or s[: i + 1] != word[: i + 1]:
                return ans
        ans = word[: i + 1]

    return ans
