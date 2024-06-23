from collections import deque


def roman_to_int(s: str) -> int:
    # letter to int mapping
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    queue = deque(list(s))
    ans = 0

    while queue:
        c = queue.popleft()  # process from left to right
        count = 1

        if queue:
            if c == "I" and d[c] < d[queue[0]] < 11:
                next = queue.popleft()
                ans += d[next] - d[c]
            elif c == "X" and d[c] < d[queue[0]] < 101:
                next = queue.popleft()
                ans += d[next] - d[c]
            elif c == "C" and d[c] < d[queue[0]]:
                next = queue.popleft()
                ans += d[next] - d[c]
            else:
                while queue and queue[0] == c:
                    count += 1
                    queue.popleft()
                ans += d[c] * count
        else:
            ans += d[c]

    return ans
