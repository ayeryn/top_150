# 5


def max_palindrome(s: str) -> str:
    if len(s) == 1:
        return s

    ans = s[0]

    for i in range(len(s)):
        # Even len palindrome
        # s[i] is the left pair
        curr = ""
        left, right = i, i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr = s[left] + curr + s[left]
            left -= 1
            right += 1
        if len(curr) > len(ans):
            ans = curr

        # Odd len palindrome
        # s[i] is the center
        left, right = i - 1, i + 1
        curr = s[i]
        while left >= 0 and right < len(s) and s[left] == s[right]:
            curr = s[left] + curr + s[left]
            left -= 1
            right += 1
        if len(curr) > len(ans):
            ans = curr

    return ans
