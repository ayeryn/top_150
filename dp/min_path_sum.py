# 64


def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if m == n == 1:
        return grid[0][0]

    def valid(x, y):
        return 0 <= x < m and 0 <= y < n

    dp = [[float("inf") for _ in range(n)] for _ in range(m)]

    # Initialize row[0] and col[0]
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        # row[0] - can only be reached from left
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    for i in range(1, m):
        # col[0] - can only be reached from up
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            # For each cell, find the min path sum to reach it

            # Got here from up
            if valid(i - 1, j):
                dp[i][j] = dp[i - 1][j] + grid[i][j]

            # Got here from left
            if valid(i, j - 1):
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])

    return dp[-1][-1]
