# 200


def islands(grid: list[list[int]]) -> int:
    ans = 0
    m, n = len(grid), len(grid[0])
    seen = set()
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == "1"

    def dfs(i, j):
        nonlocal seen
        seen.add((i, j))

        for d in dirs:
            x, y = i + d[0], j + d[1]
            if is_valid(x, y) and (x, y) not in seen:
                dfs(x, y)

    for i in range(m):
        for j in range(n):
            if (i, j) not in seen and grid[i][j] == "1":
                dfs(i, j)
                ans += 1

    return ans
