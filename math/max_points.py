# 149


from collections import defaultdict


def max_points(points: list[list[int]]) -> int:
    """
    points are on the same line if there exists a and b such that -
    y = ax + b
    """
    if len(points) == 1:
        return 1

    # (a, b) for every 2 points
    params = defaultdict(set)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            xi, yi = points[i]
            xj, yj = points[j]
            if xi == xj and yi != yj:
                # x = c (infinite slope)
                params[(xi, "b")].add((xi, yi))
                params[(xi, "b")].add((xj, yj))
            elif xi != xj and yi == yj:
                # y = b
                a = 0
                b = yi
                params[(a, b)].add((xi, yi))
                params[(a, b)].add((xj, yj))
            else:
                # a, b in natural numbers
                a = (yj - yi) / (xj - xi)
                b = yi - a * xi
                params[(a, b)].add((xi, yi))
                params[(a, b)].add((xj, yj))

    return max([len(params[k]) for k in params])
