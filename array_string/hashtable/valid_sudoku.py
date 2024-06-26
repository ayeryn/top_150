# 36
from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(9):
        for j in range(9):
            # Check row
            num = board[i][j]
            if num == ".":
                continue

            if num not in rows[i]:
                rows[i].add(num)
            else:
                return False

            # Check col
            if num not in cols[j]:
                cols[j].add(board[i][j])
            else:
                return False

            # Check square
            if num not in squares[(i // 3, j // 3)]:
                squares[(i // 3, j // 3)].add(num)
            else:
                return False

    return True
