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
