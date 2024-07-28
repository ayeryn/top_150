# 9


def palindrome(x: int) -> bool:
    # Similar to str method -> put digits in a list
    if x < 0:
        return False

    digits = []

    while x:
        digits.append(x % 10)
        x //= 10

    left, right = 0, len(digits) - 1
    while left <= right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1

    return True


def palindrome_div(x):
    if x < 0:
        return False

    if x < 10:
        return True

    div = 1
    while x > div * 10:
        # Get highest digit
        div *= 10

    while x:
        # Get first and last digits
        right = x % 10
        left = x // div
        if left != right:
            return False

        x %= div
        x //= 10
        div //= 100  # chopping 2 digits per iteration

    return True
