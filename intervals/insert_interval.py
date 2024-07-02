def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    ans = []
    start, end = newInterval
    i = 0

    while i < len(intervals) and intervals[i][1] < start:
        ans.append(intervals[i])
        i += 1

    if i == len(intervals):  # All intervals are before newInterval
        return ans + [newInterval]

    # Find start
    if intervals[i][0] <= start <= intervals[i][1]:
        start = intervals[i][0]
        # if start < intervals[i][0], start doesn't change

    # Find end
    if end < intervals[i][0]:
        # newInternal is before intervals[i]
        ans.append([start, end])  # append interval and backtrack i
        i -= 1

    elif end <= intervals[i][1]:
        ans.append([start, intervals[i][1]])
    else:
        while i < len(intervals) and end > intervals[i][1]:
            i += 1

        if i == len(intervals):
            i -= 1

        if end < intervals[i][0]:  # newInterval ends before an existing interval
            ans.append([start, end])
            i -= 1
        elif end > intervals[i][1]:  # newInterval ends after an interval
            ans.append([start, end])
        else:
            ans.append([start, intervals[i][1]])  # newInterval ends within
    return ans + intervals[i + 1 :]
