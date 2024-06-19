# 122
def stock_2(prices: list[int]) -> int:
    ans = 0

    for i in range(1, len(prices)):
        """
        If we visualize prices as a line graph, we want to get all increases.

        Note that in the case of [1,2,3,4,5], i.e., any strictly-increasing arr:
        1->5 (4) == 1->2->3->4->5 (1+1+1+1)

        [1,4,7,8,6,4]
        1->8 (7) == 1->4->7->8 (3+3+1)
        """
        profit = prices[i] - prices[i - 1]
        if profit > 0:
            ans += profit

    return ans


def stock_2_dp(prices):
    def dp(i, have_stock):
        if i == len(prices):
            return 0

        if have_stock:
            sell = prices[i] + dp(i + 1, False)
            skip = dp(i + 1, have_stock)
            return max(sell, skip)
        else:
            buy = -prices[i] + dp(i + 1, True)
            skip = dp(i + 1, have_stock)
            return max(buy, skip)

    return dp(0, False)


prices = [7, 1, 5, 3, 6, 4]
print(stock_2(prices))
print(stock_2_dp(prices))

prices = [1, 2, 3, 4, 5]
print(stock_2(prices))
print(stock_2_dp(prices))
