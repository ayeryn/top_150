# 647


def palindrome_strs(s: str) -> int:
    ans = len(s)  # base answer

    for i in range(len(s)):
        # Even len palindrome
        # s[i] is the left pair
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1

        # Odd len palindrome
        # s[i] is the center
        left, right = i - 1, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1

    return ans
