# 172


def factorial(n):
    """
    TODO: implement in code
    - 2 * 5 -> 10
    - 10 -> 10

    For every 1-10 interval, we gain 2 0's bcz
    - we have one 5
    - we have one 10

    Extra zeroes:
    - powers of 5
    - multiples of powers of 5
    - multiples of 50
    """


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
