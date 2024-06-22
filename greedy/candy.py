def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n  # everyone has at least 1

    for i in range(n):  # check in forward direction
        if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
            if candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        if i + 1 < n and ratings[i] > ratings[i + 1]:
            if candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

    for i in range(n - 1, -1, -1):  # check in backward direction
        if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
            if candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        if i + 1 < n and ratings[i] > ratings[i + 1]:
            if candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

    return sum(candies)
