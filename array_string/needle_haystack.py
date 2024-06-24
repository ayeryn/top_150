# 28


def needle_haystack(needle: str, haystack: str) -> int:
    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack)):
        if needle == haystack[i : i + len(needle)]:
            return i

    return -1
