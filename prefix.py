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
