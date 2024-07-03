# 452


def min_arrows(points: list[list[int]]) -> int:
    points.sort()
    count = 1
    s, e = points[0]

    for i in range(1, len(points)):
        if e < points[i][0]:
            s, e = points[i][0], points[i][1]
            count += 1
        else:
            e = min(e, points[i][1])  # same arrow can only go through overlapped parts
    return count
