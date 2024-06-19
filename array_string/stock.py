# 121
def stock(prices: list[int]) -> int:
    left, right = 0, 1
    ans = 0

    while right < len(prices):  # left <= right will always hold true
        curr = prices[right] - prices[left]

        if curr < 0:
            # left is too large, move on
            left += 1
        else:
            # left is small, keep searching for a larger right
            # left == right will come here thus moving right forward
            right += 1
            ans = max(ans, curr)

    return ans


def stock_prefix(prices):
    # Calculate min from left and max from right
    # O(n) memory
    left_min = [prices[0]] * len(prices)
    right_max = [prices[-1]] * len(prices)

    for i in range(1, len(prices)):  # O(n)
        left_min[i] = min(prices[i], left_min[i - 1])

    for i in range(len(prices) - 2, -1, -1):  # O(n)
        right_max[i] = max(prices[i], right_max[i + 1])

    ans = 0
    for i in range(len(prices)):  # O(n)
        # Find max right_max - left_min
        # We don't care about what prices[i] is
        ans = max(right_max[i] - left_min[i], ans)

    return ans


def stock_dp(prices):
    def dp(i, have_stock):
        if i == len(prices):
            return 0

        if have_stock:
            sell = prices[i]  # terminate recursion because 1 transaction only
            skip = dp(i + 1, have_stock)
            return max(sell, skip)
        else:
            buy = -prices[i] + dp(i + 1, True)
            skip = dp(i + 1, have_stock)
            return max(buy, skip)

    return dp(0, False)


prices = [7, 1, 5, 3, 6, 4]  # 5
print(stock(prices))
print(stock_prefix(prices))
print(stock_dp(prices))


prices = [2, 1, 4]  # 3
print(stock(prices))
print(stock_prefix(prices))
print(stock_dp(prices))

prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]  # 9
print(stock(prices))
print(stock_prefix(prices))
print(stock_dp(prices))
