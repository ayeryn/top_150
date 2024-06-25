# 125


def palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    s = s.lower()

    while left < right:
        while left < right and not s[left].isalnum():  # skip chars on left
            left += 1

        if left == len(s):  # if skipped until the end, then True
            return True

        while left < right and not s[right].isalnum():  # skip chars on right
            right -= 1

        if s[left] == s[right]:  # check alphanumeric char pairs
            left += 1
            right -= 1
        else:
            return False

    return True
