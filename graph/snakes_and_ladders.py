# 909

from collections import deque


def snakes_and_letters(board: list[list[int]]) -> int:
    n = len(board)

    def get_loc(label):
        label -= 1
        row = n - 1 - label // n
        l2r = (n % 2 == 0 and row % 2) or (n % 2 and row % 2 == 0)
        if l2r:
            col = label % n
        else:
            col = n - 1 - label % n
        return row, col

    graph = deque([1])  # BFS graph
    seen = set([1])  # keep track of visited labels
    ans = 0  # keep track of steps
    target = n**2

    while graph:
        moves = len(graph)
        for _ in range(moves):
            # Check all available moves
            label = graph.popleft()
            """
            Notes:
            1. We can't use any snakes or ladders present in the current cell
            2. When we take a snake or ladder to visit a cell, we don't count it as visited
            - Because we can visit the node from a normal move and use its snake or ladder
            """

            for x in range(label + 1, min(label + 6, target) + 1):
                if x not in seen:
                    seen.add(x)
                    i, j = get_loc(x)

                    dest = board[i][j]
                    if dest != -1:
                        x = dest
                    if x == target:
                        return ans + 1

                    graph.append(x)

        ans += 1

    # Exhausted all moves but didn't reach target => -1
    return -1


board = [[-1, -1, -1, -1], [16, 9, -1, -1], [-1, 9, 1, 1], [-1, 1, 1, -1]]
"""
16    | 15    | 14   | 13    |
9(16) | 10(9) | 11   | 12    |
8     | 7(9)  | 6(1) | 5(1)  |
1     | 2(1)  | 3(1) | 4(-1) |

1: 1 -> 4
2: 4 -> 9 -> 16
(Instead of 1 -> 7 -> 9, then 9 -> 15, then 15 -> 16)
"""
print(snakes_and_letters(board))  # 2
