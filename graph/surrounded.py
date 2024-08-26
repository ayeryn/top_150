# 130


def surrounded(board: list[list[int]]) -> None:
    # Update board in-place

    m, n = len(board), len(board[0])

    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n

    def is_border(x, y):
        return x == 0 or x == m - 1 or y == 0 or y == n - 1

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    seen = set()

    def dfs(i, j):
        nonlocal seen

        curr = board[i][j]
        seen.add((i, j))
        for n in neighbors:
            x, y = i + n[0], j + n[1]
            if is_valid(x, y) and (x, y) not in seen and board[x][y] == curr:
                dfs(x, y)

    # KEY: A region is surrounded if it can't be accessed from the borders
    for i in range(m):
        for j in range(n):
            # Run DFS on all border cells
            # Mark all border cells and cells can be accessed from border
            if (i, j) not in seen and is_border(i, j):
                dfs(i, j)

    # At this point, all regions left unmarked cannot be accessed from border
    # Thus rendering them surrounded
    for i in range(m):
        for j in range(n):
            if (i, j) not in seen and board[i][j] == "O":
                board[i][j] = "X"
