# 433

from collections import deque


def mutate(startGene: str, endGene: str, bank: list[str]) -> int:
    if startGene == endGene:
        return 0

    bank = set(bank)
    seen = set([startGene])
    steps = 0

    # Mutation graph
    mutate = {
        "A": ["C", "G", "T"],
        "C": ["A", "G", "T"],
        "G": ["A", "C", "T"],
        "T": ["A", "C", "G"],
    }

    def find_mutation(gene):
        # Find all unseen and valid mutations of gene
        ans = []
        for i in range(len(gene)):
            for mutation in mutate[gene[i]]:
                t = gene[:i] + mutation + gene[i + 1 :]
                if t in bank and t not in seen:
                    seen.add(t)
                    ans.append(t)

        return ans

    graph = deque()
    graph.append(startGene)

    while graph:
        n = len(graph)
        for _ in range(n):
            gene = graph.popleft()

            for m in find_mutation(gene):
                if m == endGene:
                    return steps + 1

                # if m not in seen:
                seen.add(m)
                graph.append(m)

        steps += 1

    # Exhausted all possible mutations and couldn't find endGene
    return -1
