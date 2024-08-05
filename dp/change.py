#

from functools import cache


def change(coins: list[int], amount: int) -> int:
    if amount == 0:  # base case
        return 0

    dp = [-1 for _ in range(amount + 1)]
    for coin in coins:
        if coin == amount:
            # if a coin is the same as amount, min is 1
            return 1
        if coin < amount:
            dp[coin] = 1

    for i in range(1, amount + 1):
        if dp[i] > 0:
            # We are building forward
            # We can only get bigger amount from i if i can be made up
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = (
                        dp[i] + 1
                        if dp[i + coin] == -1
                        else min(dp[i + coin], dp[i] + 1)
                    )

    return dp[amount]


def change_recursive(coins: list[int], amount: int) -> int:
    @cache
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1

        ans = float("inf")
        for coin in coins:
            if n == coin:
                return 1
            next = dp(n - coin)
            if next > -1:
                ans = min(ans, next + 1)

        return ans if ans != float("inf") else -1

    return dp(amount)
