# 39


def combo_sum(candidates: list[int], target: int) -> list[list[int]]:
    ans = set()

    def backtrack(i, curr_sum, curr):
        nonlocal ans
        if curr_sum == target:
            ans.add(tuple(curr))

        if curr_sum > target:
            return

        for j in range(i, len(candidates)):
            curr.append(candidates[j])

            # We can choose c[j] again, do not increase i for next call
            backtrack(j, curr_sum + candidates[j], curr)
            curr.pop()

    backtrack(0, 0, [])
    return ans
