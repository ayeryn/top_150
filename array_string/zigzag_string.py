# 6


def zigzag_string(s, rows):  # without using a mtx and join
    if rows == 1:
        return s

    n = len(s)
    mod = rows * 2 - 2
    ans = ""

    for i in range(rows):
        temp = mod - 2 * i
        for j in range(0, len(s), mod):
            if i + j < n:
                ans += s[i + j]
            if i + j + temp < n and 0 < i < rows - 1:
                ans += s[i + j + temp]
    return ans


def zigzag_string_mtx(s: str, rows: int) -> str:
    if rows == 1:
        return s

    """
    Group characters into mini-mtx, each group spans 2 columns
    1. row[0]: every rows-th character, col[1] = null
    2. row[1]: row+j, col[1] = row+j + rows*2 - 2(first and last twos have
    no col[1])
    3. row[1]: row+j, col[1] = row+j + rows*2 - 2 - 2
    ...
    n. row[rows - 1]: row + j
    """
    n = len(s)
    mod = rows * 2 - 2
    matrix = [[] for _ in range(rows)]

    for i in range(0, len(s), mod):
        matrix[0].append(s[i])
        temp = mod - 2

        for j in range(1, rows):
            if i + j < n:
                matrix[j].append(s[i + j])
            if i + j + temp < n and j < rows - 1 and temp:
                matrix[j].append(s[i + j + temp])
            temp -= 2

    ans = ""
    for row in matrix:
        ans += "".join(row)  # join all rows together
    return ans
