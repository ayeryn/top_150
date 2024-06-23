# 58


def len_last_word(s: str) -> int:
    right = len(s) - 1

    while right >= 0:  # process forward
        while right >= 0 and s[right] == " ":
            # skip trailing blanks
            right -= 1

        # Edge cases
        if right == 0:
            return 1
        if right < 0:
            return 0

        left = right - 1
        while left >= 0 and s[left] != " ":
            left -= 1

        return right - left
