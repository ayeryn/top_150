# 127

from collections import deque, defaultdict


def ladder(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if beginWord == endWord:
        return 0

    ladder = defaultdict(list)
    # Build adjacency graph
    # Utilize "*" and avoid checking possible chars for position
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1 :]
            ladder[pattern].append(word)

    seen = set([beginWord])
    graph = deque([beginWord])
    steps = 1  # First word counts as part of the ladder

    while graph:
        n = len(graph)
        for _ in range(n):
            word = graph.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                for w in ladder[pattern]:
                    # Check ladder patten graph for available words
                    if w != word and w not in seen:
                        graph.append(w)
                        seen.add(w)

        steps += 1

    return 0
