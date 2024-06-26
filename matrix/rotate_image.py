# 48


def rotate_image(matrix: list[list[int]]) -> None:
    """
    Rotate in-place
    """
    n = len(matrix)
    l, r = 0, n - 1

    while l < r:
        top, bottom = l, r
        for pos in range(r - l):
            # save top_left
            top_left = matrix[top][l + pos]

            # move bottom left to top left
            # another pos RIGHT
            matrix[top][l + pos] = matrix[bottom - pos][l]

            # move bottom right to bottom left
            # another pos UP
            matrix[bottom - pos][l] = matrix[bottom][r - pos]

            # move top right to bottom right
            # another pos LEFT
            matrix[bottom][r - pos] = matrix[top + pos][r]

            # move top_left to top right
            # another pos DOWN
            matrix[top + pos][r] = top_left

        l += 1
        r -= 1
