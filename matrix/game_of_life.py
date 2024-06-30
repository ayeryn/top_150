# 289


def game(board):
    """
    Do not return anything, modify board in-place instead.
    """
    nbs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    m, n = len(board), len(board[0])

    def valid(x, y):
        return 0 <= x < m and 0 <= y < n

    def new_val(old, new):
        """
        We need old[0] = 0 and old[1] = 1
        old | new | val
        0   | 0   | 0
        1   | 0   | 1
        0   | 1   | 2
        1   | 1   | 3
        """
        if not old and not new:
            return 0
        if old and not new:
            return 1
        if not old and new:
            return 2
        if old and new:
            return 3

    # mapping for old and new values
    old_mapping = {0: 0, 1: 1, 2: 0, 3: 1}
    new_mapping = {0: 0, 1: 0, 2: 1, 3: 1}

    for i in range(m):  # O(m)
        for j in range(n):  # O(n)
            old_val = board[i][j]
            count = 0
            for nb in nbs:  # O(1)
                x, y = i + nb[0], j + nb[1]
                if valid(x, y):
                    count += old_mapping[board[x][y]]
            if count < 2:
                board[i][j] = new_val(old_val, old_mapping[0])
            elif 2 <= count <= 3 and old_val:
                board[i][j] = new_val(old_val, old_mapping[1])
            elif count > 3 and old_val:
                board[i][j] = new_val(old_val, old_mapping[0])
            elif count == 3 and not old_val:
                board[i][j] = new_val(old_val, old_mapping[1])

    for i in range(m):
        for j in range(n):
            board[i][j] = new_mapping[board[i][j]]


def game_mem(board: list[list[int]]) -> None:
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
            cache[(i, j)] = live0
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
