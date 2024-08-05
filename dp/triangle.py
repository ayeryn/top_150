# 120

from functools import cache


def triangle_sum(triangle: list[list[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]

    m, n = len(triangle), len(triangle[-1])
    dp = [[float("inf") for _ in range(n)] for _ in range(m)]
    dp[0][0] = triangle[0][0]

    curr_col = 1  # max col for each row
    for row in range(0, m - 1):
        for col in range(curr_col):
            dp[row + 1][col] = min(
                dp[row + 1][col], triangle[row + 1][col] + dp[row][col]
            )
            dp[row + 1][col + 1] = min(
                dp[row + 1][col + 1], triangle[row + 1][col + 1] + dp[row][col]
            )
        curr_col += 1  # Increase max col for next row

    return min(dp[-1])


def triangle_recursive(triangle):
    @cache
    def dp(row, col):
        if row == len(triangle):
            return 0

        ret = dp(row + 1, col)
        if col <= row:
            ret = min(ret, dp(row + 1, col + 1))

        return ret + triangle[row][col]

    return dp(0, 0)
