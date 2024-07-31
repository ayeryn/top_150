# 188


def stock(prices: list[int], k: int) -> int:
    # ki => i transactions
    k_buy = [float("-inf") for _ in range(k)]
    k_sell = [0 for _ in range(k)]

    for p in prices:
        # Base case - one transaction only
        k_buy[0] = max(k_buy[0], -p)
        k_sell[0] = max(k_sell[0], k_buy[0] + p)

        for i in range(1, k):
            k_buy[i] = max(k_buy[i], -p + k_sell[i - 1])
            k_sell[i] = max(k_sell[i], k_buy[i] + p)

    return max(k_sell)
