# 66


def plusOne(digits: list[int]) -> list[int]:
    d_sum = 1
    for i in range(len(digits) - 1, -1, -1):
        d_sum += digits[i]

        digits[i] = d_sum % 10
        d_sum //= 10
        if d_sum == 0:
            # Terminate early when nothing to carry over
            return digits

    return [1] + digits
