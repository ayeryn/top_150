# 123


from functools import cache


def max_profit(prices):
    """
    We can make at most transactions so there are 3 cases:
    1. 0 transactions
    2. 1 transaction
    3. 2 transactions
    """
    one_buy = float("-inf")
    one_buy_one_sell = 0
    two_buy = float("-inf")
    two_buy_two_sell = 0

    for p in prices:
        """
        buying -> -p; selling -> +p
        """
        one_buy = max(one_buy, -p)
        one_buy_one_sell = max(one_buy_one_sell, one_buy + p)
        two_buy = max(two_buy, one_buy_one_sell - p)
        two_buy_two_sell = max(two_buy_two_sell, two_buy + p)

    return (one_buy_one_sell, two_buy_two_sell)


def max_profit_dp(prices: list[int]) -> int:
    @cache
    def dp(i, count):
        # even count -> no stock, odd count -> have stock
        if i == len(prices) or not count:
            return 0

        if count % 2:
            keep = dp(i + 1, count)
            sell = prices[i] + dp(i + 1, count - 1)
            return max(keep, sell)
        else:
            buy = -prices[i] + dp(i + 1, count - 1)
            skip = dp(i + 1, count)
            return max(buy, skip)

    return dp(0, 4)
