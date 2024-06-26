def set_zeroes(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    cols = set()
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            # mark rows and cols that need to be 0
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            # set 0s
            if i in rows or j in cols:
                matrix[i][j] = 0
