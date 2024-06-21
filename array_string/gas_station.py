def gas_station(gas, cost):
    prefix = []
    p_sum = 0
    n = len(gas)

    for i in range(n):
        distance = gas[i] - cost[i]
        prefix.append(distance)
        p_sum += distance

    if p_sum < 0:
        return -1

    left = 0
    total = 0
    start = 0
    for i in range(n):
        total += prefix[i]

        if total < 0:
            left += total
            total = 0
            start = i + 1

    return start


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
