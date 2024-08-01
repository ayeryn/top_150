# 127

from collections import deque


def ladder(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if beginWord == endWord:
        return 0

    wordList = set(wordList)

    def process_chars():
        # Put all valid chars in a set
        s = set()
        for word in wordList:
            for c in word:
                if c not in s:
                    s.add(c)
        return s

    valid_chars = process_chars()

    seen = set([beginWord])

    def change(word):
        ans = []
        for i in range(len(word)):
            for c in valid_chars:
                if c != word[i]:
                    temp = word[:i] + c + word[i + 1 :]
                    if temp not in seen and temp in wordList:
                        # Add possible changed word to ans
                        ans.append(temp)
                        seen.add(temp)

        return ans

    graph = deque([beginWord])
    steps = 1  # First word counts as part of the ladder

    while graph:
        n = len(graph)
        for _ in range(n):
            word = graph.popleft()

            for w in change(word):
                if w == endWord:
                    return steps + 1
                graph.append(w)

        steps += 1

    return 0
