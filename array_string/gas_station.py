def gas_station(gas, cost):
    """
    We are calculating "prefix" and checking validity in one pass.
    - Still O(n) but O(1) memory

    Think about the starting index as a pivot.
    - Total distance traveled must be >= 0 to progress
    - When total becomes negative, we know the answer is a later index, and distance_traveled becomes distance_left_to_travel
    """
    n = len(gas)
    left = 0  # distance left to travel
    total = 0  # distance traveled
    start = 0  # starting index
    for i in range(n):
        distance = gas[i] - cost[i]  # distance at current index
        total += distance  # update total distance traveled

        if total < 0:
            # cannot progress, convert distance_traveled to left_to_travel
            left += total
            total = 0  # reset total
            start = i + 1  # update pivot

    return -1 if left + total < 0 else start


def gas_station_brute(gas: list[int], cost: list[int]) -> int:
    n = len(gas)

    def traverse(i):
        distance = 0
        for x in range(n):
            ind = (i + x) % n
            distance += gas[ind] - cost[ind]

            if distance < 0:
                return False
        return True

    for i in range(n):
        if gas[i] - cost[i] >= 0 and traverse(i):
            return i
    return -1
