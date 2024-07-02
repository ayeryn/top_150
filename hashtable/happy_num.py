# 202


def is_happy(n: int) -> bool:
    def sum_digits(x):  # sum and square digits
        ret = 0
        while x:
            ret += (x % 10) ** 2
            x //= 10

        return ret

    seen = set()  # keep track of all sums
    while n != 1:
        if n in seen:  # once we are in a cycle, return False
            return False

        seen.add(n)
        n = sum_digits(n)

    return True
