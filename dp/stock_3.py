# 123


from functools import cache


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
