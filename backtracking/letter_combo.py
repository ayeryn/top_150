# 17


def letter_combo(digits: str) -> list[list[str]]:
    if len(digits) == 0:
        return []

    combos = {
        # Can also be a string
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    ans = []

    def solve(i, sol):
        nonlocal ans

        if i == len(digits):
            ans.append(sol[:])
            return

        for c in combos[digits[i]]:
            solve(i + 1, sol + c)

    solve(0, "")
    return ans
