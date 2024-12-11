from collections import deque

class TrailMap:
    def __init__(self, file) -> None:
        with open(file) as f:
            rows = f.read().splitlines()
        self.map = [[int(c) for c in row] for row in rows]
        self.trail_heads = []
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 0:
                    self.trail_heads.append((i, j))

    def slope_neighbors(self, i: int, j: int) -> list[tuple[int, int]]:
        neighbors = []
        if i > 0 and self.map[i - 1][j] == self.map[i][j] + 1:
            neighbors.append((i - 1, j))
        if i < len(self.map) - 1 and self.map[i + 1][j] == self.map[i][j] + 1:
            neighbors.append((i + 1, j))
        if j > 0 and self.map[i][j - 1] == self.map[i][j] + 1:
            neighbors.append((i, j - 1))
        if j < len(self.map[0]) - 1 and self.map[i][j + 1] == self.map[i][j] + 1:
            neighbors.append((i, j + 1))
        return neighbors
    
    def find_summits(self, trail_head: tuple[int, int]) -> list[tuple[int, int]]:
        queue = deque([trail_head])
        visited = set()
        visited.add(trail_head)
        summits = []
        while queue:
            i, j = queue.popleft()
            if self.map[i][j] == 9:
                summits.append((i, j))
            neighbors = self.slope_neighbors(i, j)
            for n in neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
        return summits
    
    def find_trails(self, trail_head: tuple[int, int], summit: tuple[int, int]) -> list[tuple[int, int]]:
        queue = deque([[trail_head]])
        trails = []
        while queue:
            path = queue.popleft()
            i, j = path[-1]
            if (i, j) == summit:
                trails.append(path)
            neighbors = self.slope_neighbors(i, j)
            for n in neighbors:
                new_path = path[:]
                new_path.append(n)
                queue.append(new_path)
        return trails

trail_map = TrailMap('2024/input/day10')

print("Part 1:", sum([len(trail_map.find_summits(th)) for th in trail_map.trail_heads]))

print("Part 2:", sum([sum([len(trail_map.find_trails(th, s)) for s in trail_map.find_summits(th)]) for th in trail_map.trail_heads]))
