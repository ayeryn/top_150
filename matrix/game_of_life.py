def game(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    nbs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    m, n = len(board), len(board[0])

    def valid(x, y):
        return 0 <= x < m and 0 <= y < n

    cache = {}  # cache changed cells

    for i in range(m):
        for j in range(n):
            live = board[i][j]
            cache[(i, j)] = live
            count = 0
            for nb in nbs:
                x, y = i + nb[0], j + nb[1]
                if valid(x, y):
                    if (x, y) in cache:
                        count += cache[(x, y)]
                    else:
                        count += board[x][y]
            if count < 2:
                board[i][j] = 0
            elif 2 <= count <= 3 and live:
                board[i][j] = 1
            elif count > 3 and live:
                board[i][j] = 0
            elif count == 3 and not live:
                board[i][j] = 1


def game_mem(board):
    nbs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    m, n = len(board), len(board[0])

    def valid(x, y):
        return 0 <= x < m and 0 <= y < n

    ret = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            live = board[i][j]
            count = 0
            for nb in nbs:
                x, y = i + nb[0], j + nb[1]
                if valid(x, y) and board[x][y]:
                    count += 1
            if count < 2:
                ret[i][j] = 0
            elif 2 <= count <= 3 and live:
                ret[i][j] = 1
            elif count > 3 and live:
                ret[i][j] = 0
            elif count == 3 and not live:
                ret[i][j] = 1
    return ret
