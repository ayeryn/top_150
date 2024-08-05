# 50


def pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    ans = 1

    if n < 0:
        x = 1 / x
        n = -n

    while n >= 1:
        ans *= x
        n -= 1
    return ans
