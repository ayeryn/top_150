# 49


def group_anagram(strs: list[str]) -> list[list[str]]:
    d = {}

    def count_chars(s):  # count char and return counter as tuple
        count = [0] * 26
        for i in range(0, 27):
            count[ord(c) - ord("a")] += 1

        return tuple(count)

    for s in strs:
        c = count_chars(s)
        if c not in d:
            d[c] = [s]
        else:
            d[c].append(s)

    return d.values()
