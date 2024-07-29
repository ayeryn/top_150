# 77


def combination(n: int, k: int) -> list[list[int]]:
    def solve(curr, i):
        if len(curr) == k:
            # terminate when we have picked k numbers
            ans.append(curr[:])

        for x in range(i, n + 1):
            # process inorder to make sure 
            solve(curr + [x], x + 1)

    ans = []
    solve([], 1)
    return ans
