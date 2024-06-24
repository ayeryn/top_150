def reverse_words(s: str) -> str:
    l = []
    i = len(s) - 1

    while i >= 0:
        # Skip leading space
        while i >= 0 and s[i] == " ":
            i -= 1

        if i < 0:
            break

        # Find the next word
        left = i - 1
        while left >= 0 and s[left] != " ":
            left -= 1

        if left < 0:
            l.append(s[: i + 1])
        else:
            l.append(s[left + 1 : i + 1])

        i = left  # Progress i

    return " ".join(l)
