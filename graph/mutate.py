# 433

from collections import deque, defaultdict


def mutate(startGene: str, endGene: str, bank: list[str]) -> int:
    if startGene == endGene:
        return 0

    bank = set(bank)
    seen = set([startGene])
    steps = 0
    graph = deque([startGene])

    # Construct adjacency list from bank
    # to avoid invalid gene mutations
    mutation = defaultdict(list)
    for gene in bank:
        for i in range(len(gene)):
            pattern = gene[:i] + "*" + gene[i + 1 :]
            mutation[pattern].append(gene)

    while graph:
        n = len(graph)
        for _ in range(n):
            gene = graph.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                pattern = gene[:i] + "*" + gene[i + 1 :]
                for g in mutation[pattern]:
                    # Check against all VALID mutations
                    if g != gene and gene not in seen:
                        seen.add(g)
                        graph.append(g)

        steps += 1

    # Exhausted all possible mutations and couldn't find endGene
    return -1
