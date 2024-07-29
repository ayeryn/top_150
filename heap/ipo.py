# 502

from heapq import heappush, heappop


def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:

    # Sort project by capital
    # Zip capital and profits to maintain index order
    projects = sorted(list(zip(capital, profits)))
    heap = []
    i = count = 0

    while count < k:  # Choose at most k projects
        while i < len(projects) and projects[i][0] <= w:
            # Add profit of all doable projects to heap as w updates
            # Maintain a max heap
            heappush(heap, -projects[i][1])
            i += 1

        if not heap:
            # No doable projects, terminate early
            return w

        # Pick project with most profit
        p = heappop(heap)
        w -= p
        count += 1

    return w
