# 190


def reverse_bits(n: int) -> int:
    ret = 0

    for i in range(32):
        last_bit = n & 1  # Get last bit

        ret <<= 1  # Shift ret left to add a 0 bit at the end
        if last_bit:
            # Add 1 at lowest bit
            ret |= 1
        n >>= 1  # Truncate last bit of n

    return ret
