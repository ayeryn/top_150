# 70


def stairs(n: int) -> int:
    # Another form of Fibonacci
    if n == 1 or n == 2:
        return n

    s1, s2 = 1, 2
    for _ in range(3, n + 1):
        temp = s1 + s2
        s1 = s2
        s2 = temp

    return s2
