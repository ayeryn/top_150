# 399

from collections import defaultdict, deque
from typing import List


def evaluate_division(
    equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:

    ans = [-1.0 for _ in range(len(queries))]

    graph = defaultdict(set)
    vals = {}

    # Construct graph (undirected)
    for i in range(len(equations)):
        x, y = equations[i]
        graph[x].add(y)
        graph[y].add(x)
        vals[(x, y)] = values[i]
        vals[(y, x)] = 1 / values[i]

    for i in range(len(queries)):
        x, y = queries[i]
        if x not in graph or y not in graph:
            # query var not in equations
            continue
        elif x == y:
            ans[i] = 1.0
        elif y in graph[x]:
            ans[i] = vals[(x, y)]
        else:
            # BFS
            seen = set()  # Avoid infinite loop

            # Define search space, keep track of quotient
            sol = deque([(x, 1.0)])
            found = False
            while len(sol) > 0 and not found:
                nums = len(sol)
                for _ in range(nums):
                    num, q = sol.popleft()
                    if num == y:
                        # Found divisor
                        ans[i] = q
                        found = True  # Make sure to terminate while loop
                        break  # Terminate for loop
                    elif num not in seen:
                        seen.add(num)
                        for j in graph[num]:
                            # Ensure quotient is updated
                            sol.append((j, q * vals[(num, j)]))

    return ans
