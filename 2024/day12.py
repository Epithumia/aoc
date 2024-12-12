from collections import deque


class GardenRegion:
    def __init__(self, type) -> None:
        self.tiles = []
        self.type = type
        self.sides = {"n": set(), "s": set(), "w": set(), "e": set()}

    def add_tile(self, tile) -> None:
        self.tiles.append(tile)

    def perimeter(self) -> int:
        return sum([len(self.edges(t)) for t in self.tiles])

    def edges(self, tile) -> int:
        edges = []
        if (tile[0] - 1, tile[1]) not in self.tiles:
            edges.append("n")
            self.sides["n"].add(tile)
        if (tile[0] + 1, tile[1]) not in self.tiles:
            edges.append("s")
            self.sides["s"].add(tile)
        if (tile[0], tile[1] - 1) not in self.tiles:
            edges.append("w")
            self.sides["w"].add(tile)
        if (tile[0], tile[1] + 1) not in self.tiles:
            edges.append("e")
            self.sides["e"].add(tile)
        return edges

    def surface(self) -> int:
        return len(self.tiles)

    def count_sides(self) -> int:
        sides = 0
        edges = ["n", "s", "w", "e"]
        x = {"n": 0, "s": 0, "e": 1, "w": 1}
        y = {"n": 1, "s": 1, "e": 0, "w": 0}
        for edge in edges:
            candidates = set(t for t in self.sides[edge])
            while len(candidates) > 0:
                tile = candidates.pop()
                chain = deque()
                chain.append(tile)
                while True:
                    if (chain[0][0] - x[edge], chain[0][1] - y[edge]) in candidates:
                        candidates.remove(
                            (chain[0][0] - x[edge], chain[0][1] - y[edge])
                        )
                        chain.appendleft((chain[0][0] - x[edge], chain[0][1] - y[edge]))
                    elif (chain[-1][0] + x[edge], chain[-1][1] + y[edge]) in candidates:
                        candidates.remove(
                            (chain[-1][0] + x[edge], chain[-1][1] + y[edge])
                        )
                        chain.append((chain[-1][0] + x[edge], chain[-1][1] + y[edge]))
                    else:
                        break
                sides += 1
        return sides


class Garden:
    def __init__(self, file) -> None:
        with open(file) as f:
            data = f.read().splitlines()
        self.grid = [[c for c in row] for row in data]
        self.regions = []
        to_map = set()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                to_map.add((i, j))

        while len(to_map) > 0:
            tile = to_map.pop()
            neighbors = [tile]
            r = GardenRegion(self.grid[tile[0]][tile[1]])
            while len(neighbors) > 0:
                tile = neighbors.pop()
                r.add_tile(tile)
                for n in [
                    (tile[0] - 1, tile[1]),
                    (tile[0] + 1, tile[1]),
                    (tile[0], tile[1] - 1),
                    (tile[0], tile[1] + 1),
                ]:
                    if (
                        n in to_map
                        and self.grid[n[0]][n[1]] == self.grid[tile[0]][tile[1]]
                    ):
                        neighbors.append(n)
                        to_map.remove(n)
            self.regions.append(r)

    def cost(self) -> int:
        return sum([r.surface() * r.perimeter() for r in self.regions])

    def bulk_cost(self) -> int:
        return sum([r.surface() * r.count_sides() for r in self.regions])


garden = Garden("2024/input/day12")

print("Part 1:", garden.cost())
print("Part 2:", garden.bulk_cost())
