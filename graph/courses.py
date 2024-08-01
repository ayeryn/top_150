# 207

from collections import defaultdict


def courses(courses: int, prereq: list[list[int]]) -> bool:
    graph = defaultdict(list)
    taken = set()

    for a, b in prereq:
        graph[a].append(b)

    for i in range(courses):
        # FIXME: don't need to take courses in-order
        if i not in graph or any([p in taken for p in graph[i]]):
            taken.add(i)
        else:
            return False

    return True
