# 54


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    if len(matrix) == 1:  # edge case
        return matrix[0]

    ans = []
    visited = set()  # visited indices
    m, n = len(matrix), len(matrix[0])

    # current direction -> next_direction
    dmap = {"right": "down", "down": "left", "left": "up", "up": "right"}
    d = "right"  # start with right
    i = j = 0  # start at matrix[0][0]

    while len(visited) < m * n:
        if d == "right":
            while j < n and (i, j) not in visited:
                visited.add((i, j))
                ans.append(matrix[i][j])
                j += 1  # traverse right
            j -= 1  # bring j back inbound
            i += 1  # move i to next position

        elif d == "down":
            while i < m and (i, j) not in visited:
                visited.add((i, j))
                ans.append(matrix[i][j])
                i += 1  # traverse down
            i -= 1  # bring i back inbound
            j -= 1  # move j to next position

        elif d == "left":
            while j >= 0 and (i, j) not in visited:
                visited.add((i, j))
                ans.append(matrix[i][j])
                j -= 1  # traverse left
            j += 1  # bring j back inbound
            i -= 1  # move i to next position

        else:  # up
            while i >= 0 and (i, j) not in visited:
                visited.add((i, j))
                ans.append(matrix[i][j])
                i -= 1  # traverse up
            i += 1  # bring i back inbound
            j += 1  # move j to next position

        d = dmap[d]  # change direction

    return ans
