from collections import Counter
from itertools import combinations
from math import dist


pairs = []
points = []
networks = {}
n = 0

with open("2025/input/day08") as f:
    data = f.read().splitlines()

    for line in data:
        x = tuple(int(x) for x in line.split(","))
        points.append(x)
        networks[x] = n
        n += 1


for p1, p2 in combinations(points, 2):
    distance = dist(p1, p2)
    pairs.append((distance, p1, p2))

pairs.sort()

wires = 1000

for d, p1, p2 in pairs:
    n1, n2 = networks[p1], networks[p2]
    if n1 != n2:
        for p in points:
            if networks[p] == n2:
                networks[p] = n1
    wires -= 1

    if wires == 0:
        network_sizes = Counter(networks.values())
        largest = network_sizes.most_common(3)
        print("Partie 1:", largest[0][1] * largest[1][1] * largest[2][1])

    if len(set(networks.values())) == 1:
        print("Partie 2:", p1[0] * p2[0])
        break
