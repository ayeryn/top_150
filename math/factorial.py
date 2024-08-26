# 172


def factorial(n):
    """
    1. We get a 0 every time we have a 5 (2 appears more often than 5 and 2*5 = 10)
    2. We gain extra zeroes when we encounter:
      - powers of 5
      - multiples of powers of 5
    """

    # Since n <= 10**4, we need the largest power of 5 <= 10**4 (5**5 = 3126)
    powers = [5**i for i in range(1, 6)]
    count = 0

    for p in powers:
        """
        p = 5: every multiples of 5 gains one 0
        p = 25: gain an extra
        p = 125: gain an extra
        ...
        """
        count += n // p

    return count


def factorial_brute(n: int) -> int:
    product = 1

    while n:  # Calculate factorial
        product *= n
        n -= 1

    count = 0
    while product:
        # Get trailing zeroes
        if product % 10 == 0:
            count += 1
            product //= 10
        else:
            break

    return count
