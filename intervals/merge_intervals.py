def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()  # sort by start
    ans = []
    start, end = intervals[0]
    i = 1

    while i < len(intervals):
        if intervals[i][0] > end:
            ans.append([start, end])
            start, end = intervals[i]
        elif intervals[i][1] > end:
            end = intervals[i][1]

        i += 1
    ans.append([start, end])

    return ans
