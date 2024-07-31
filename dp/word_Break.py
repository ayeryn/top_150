# 139


def word_break(s: str, word_dict: list[str]) -> bool:
    d = set(word_dict)
    if s in d:
        return True

    dp = [False for _ in range(len(s))]
    words_ind = []

    for i in range(len(s)):
        # s[: i+1]
        # s[:j+1] where j < 1 and s[j+1:i+1]
        dp[i] = s[: i + 1] in d or any([s[ind + 1 : i + 1] in d for ind in words_ind])
        if dp[i]:
            words_ind.append(i)

    return dp[-1]
