# 79


def word_search(board: list[list[int]], word: str) -> bool:
    m, n = len(board), len(board[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def valid(x, y):
        return 0 <= x < m and 0 <= y < n

    def backtrack(i, j, wi, visited):
        if wi == len(word):
            return True

        for d in dirs:
            x, y = i + d[0], j + d[1]
            if valid(x, y) and (x, y) not in visited and board[x][y] == word[wi]:
                # Only continue if current char matches word[wi]
                visited.add((x, y))
                if backtrack(x, y, wi + 1, visited):
                    return True
                visited.remove((x, y))

        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and backtrack(i, j, 1, set([(i, j)])):
                return True

    return False
