# 191


def hamming_weight(n: int) -> int:
    # Use the erase lowest set bit trick
    result = 0

    while n:
        result += 1
        n &= n - 1

    return result
