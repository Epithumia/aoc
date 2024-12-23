from collections import defaultdict
from itertools import combinations

graph = defaultdict(lambda: set())

with open("2024/input/day23") as f:
    data = f.read().splitlines()

    for line in data:
        nodes = line.split("-")
        graph[nodes[0]].add(nodes[1])
        graph[nodes[1]].add(nodes[0])


part1 = 0
for triplet in combinations(graph.keys(), 3):
    n1, n2, n3 = triplet
    if (
        n2 in graph[n1]
        and n2 in graph[n3]
        and n3 in graph[n1]
        and n3 in graph[n2]
        and n1 in graph[n2]
        and n1 in graph[n3]
        and ("t" in [n1[0], n2[0], n3[0]])
    ):
        part1 += 1

print("Part 1:", part1)

best_clique = []
for k in graph.keys():
    clique = list()
    clique.append(k)
    for k2 in graph.keys():
        if k != k2 and all([k2 in graph[c] for c in clique]):
            clique.append(k2)
    if len(clique) > len(best_clique):
        best_clique = sorted(clique)

print("Part 2:", ",".join(best_clique))
