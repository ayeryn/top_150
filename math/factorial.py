# 172


def factorial(n: int) -> int:
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
