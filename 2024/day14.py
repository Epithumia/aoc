from parse import parse
from collections import defaultdict

h = 103
w = 101

robots = []

with open("2024/input/day14") as f:
    data = f.read().splitlines()

    for line in data:
        r = parse("p={px:d},{py:d} v={vx:d},{vy:d}", line)
        robots.append((r["px"], r["py"], r["vx"], r["vy"]))

quarters = [0, 0, 0, 0]

for px, py, vx, vy in robots:
    rx = (px + 100 * vx) % w
    ry = (py + 100 * vy) % h
    if rx < (w - 1) / 2 and ry < (h - 1) / 2:
        quarters[0] += 1
    if (w - 1) / 2 < rx and ry < (h - 1) / 2:
        quarters[1] += 1
    if rx < (w - 1) / 2 and (h - 1) / 2 < ry:
        quarters[2] += 1
    if (w - 1) / 2 < rx and (h - 1) / 2 < ry:
        quarters[3] += 1

print("Part 1:", quarters[0] * quarters[1] * quarters[2] * quarters[3])


def flood_fill(picture):
    queue = set([(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)])
    while len(queue) > 0:
        x, y = queue.pop()
        if picture[(x, y)] == 0:
            picture[(x, y)] = 1
            if x > 0 and picture[(x - 1, y)] == 0:
                queue.add((x - 1, y))
            if x < w - 1 and picture[(x + 1, y)] == 0:
                queue.add((x + 1, y))
            if y > 0 and picture[(x, y - 1)] == 0:
                queue.add((x, y - 1))
            if y < h - 1 and picture[(x, y + 1)] == 0:
                queue.add((x, y + 1))


for i in range(10000):
    final = defaultdict(lambda: 0)
    check = defaultdict(lambda: 0)
    for px, py, vx, vy in robots:
        rx = (px + i * vx) % w
        ry = (py + i * vy) % h
        final[(rx, ry)] = 1
        check[(rx, ry)] += 1

    if all([check[(x, y)] == final[(x, y)] for x,y in final]):
        print("Part 2:", i)
        break

    # Original idea below:
    # flood_fill(final)
    # # The right image will have more empty space because the tree is framed in a square
    # if sum([final[(x, y)] for x in range(w) for y in range(h)]) < w * h - 50:
    #     print("Part 2:", i)
    #     break
