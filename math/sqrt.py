# 69


def sqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x

    for i in range(1, x // 2 + 2):
        if i * i == x:
            return i

        if i * i > x:
            return i - 1
