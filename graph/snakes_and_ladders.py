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

            label = graph.popleft()  # Check all available moves
            if label == target:
                return ans  # reached target, terminate function

            for x in range(label + 1, min(label + 6, target) + 1):
                # Get next moves if they haven't been visited
                if x not in seen:
                    seen.add(x)
                    i, j = get_loc(x)

                    # Check for snakes and ladders
                    dest = board[i][j]
                    if dest == -1:
                        graph.append(x)
                    else:
                        graph.append(dest)
                        seen.add(dest)

        ans += 1

    # Exhausted all moves but didn't reach target => -1
    return -1
