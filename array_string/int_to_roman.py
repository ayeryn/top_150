# 12


def int_to_roman(nums: int) -> str:
    # five and ten mapping to one
    d = {"V": "I", "X": "I", "L": "X", "C": "X", "D": "C", "M": "C"}
    ans = ""
    stack = ["M", "D", "C", "L", "X", "V", "I"]

    while num:  # process digits from right to left
        digit = num % 10
        one = stack.pop()
        five = stack.pop() if stack else ""
        ten = stack[-1] if stack else ""

        if digit <= 3:
            ans = one * digit + ans
        elif digit == 4:
            ans = d[five] + five + ans
        elif digit == 5:
            ans = five + ans
        elif 6 <= digit < 9:
            ans = five + one * (digit - 5) + ans
        elif digit == 9:
            ans = one + ten + ans

        num = num // 10

    return ans
