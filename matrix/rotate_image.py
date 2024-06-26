# 48


def rotate_image(matrix: list[list[int]]) -> None:
    """
    Rotate in-place
    """
    n = len(matrix)
    l, r = 0, n - 1

    while l < r:
        for pos in range(l, r):
            i, j = l, l + pos
            curr = matrix[i][j]

            # left to right
            i, j = pos, r
            temp = matrix[i][j]
            matrix[i][j] = curr
            print(f"({i}, {j}): {temp} => {curr}")
            curr = temp

            # right to down
            i, j = r, r - pos
            temp = matrix[i][j]
            matrix[i][j] = curr
            print(f"({i}, {j}): {temp} => {curr}")
            curr = temp

            # down to left
            i, j = r - pos, l
            temp = matrix[i][j]
            matrix[i][j] = curr
            print(f"({i}, {j}): {temp} => {curr}")
            curr = temp

            # left to up
            i, j = l, l + pos
            temp = matrix[i][j]
            matrix[i][j] = curr
            print(f"({i}, {j}): {temp} => {curr}\n")
            curr = temp

        l += 1
        r -= 1
