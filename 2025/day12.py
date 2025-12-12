import pulp
import itertools


def covered(tile, base):
    return {(base[0] + t[0], base[1] + t[1]): True for t in tile}


def flip(present):
    return [(2 - x, 2 - y) for (x, y) in present]


def rotate(present, n):
    if n == 0:
        return present
    if n == 1:
        return [(2 - y, x) for (x, y) in present]
    return rotate(present, n - 1)


def solve(presents, area):
    tiles = []
    for p in presents:
        for i in range(4):
            tiles.append(rotate(p.copy(), i))
            tiles.append(flip(rotate(p.copy(), i)))
    rows = area["y"]
    cols = area["x"]
    squares = {x: True for x in itertools.product(range(rows), range(cols))}
    vars = list(itertools.product(range(rows), range(cols), range(len(tiles))))
    vars = [
        x
        for x in vars
        if all([y in squares for y in covered(tiles[x[2]], (x[0], x[1])).keys()])
    ]
    x = pulp.LpVariable.dicts("tiles", vars, lowBound=0, upBound=1, cat=pulp.LpInteger)
    mod = pulp.LpProblem("polyominoes", pulp.LpMaximize)
    mod += sum([len(tiles[p[2]]) * x[p] for p in vars])
    # Use each shape n times
    for i in range(len(tiles) // 8):
        mod += (
            sum([x[p] for p in vars if p[2] in list(range(i * 8, (i + 1) * 8))])
            == area["n"][i]
        )
    # Each square can be covered by at most one shape
    for s in squares:
        mod += sum([x[p] for p in vars if s in covered(tiles[p[2]], (p[0], p[1]))]) <= 1

    mod.solve(pulp.PULP_CBC_CMD(msg=0))

    if mod.status > 0:
        import string

        out = [["-"] * cols for rep in range(rows)]
        chars = string.ascii_uppercase + string.ascii_lowercase
        numset = 0
        for p in vars:
            if x[p].value() == 1.0:
                for off in tiles[p[2]]:
                    out[p[0] + off[0]][p[1] + off[1]] = chars[numset]
                numset += 1
        for row in out:
            print("".join(row))

    return mod.status


with open("2025/input/day12test") as f:
    data = f.read().splitlines()

    presents_data = {}
    area = {}

    area_id = 1

    for row in data:
        if ":" in row and "x" not in row:
            present_id = int(row.split(":")[0])
            presents_data[present_id] = []
        if present_id is not None and ":" not in row and len(row) > 0:
            presents_data[present_id].append(row)
        if ":" in row and "x" in row:
            present_id = None
            area[area_id] = {
                "x": int(row.split("x")[0]),
                "y": int(row.split("x")[1].split(":")[0]),
                "s": int(row.split("x")[0]) * int(row.split("x")[1].split(":")[0]),
                "n": [int(x) for x in row.split("x")[1].split(":")[1][1:].split(" ")],
            }
            area_id += 1

    presents = []
    for present_id in presents_data.keys():
        p = []
        for j in range(len(presents_data[present_id])):
            for i in range(len(presents_data[present_id][j])):
                if presents_data[present_id][j][i] == "#":
                    p.append((i, j))
        presents.append(p)
    ok = 0
    for a in area:
        loose_surface = (area[a]["x"] - area[a]["x"] % 3) * (
            area[a]["y"] - area[a]["y"] % 3
        )  # area[a]["s"]
        surface_presents = 0
        loose_space = 0
        for i in range(len(area[a]["n"])):
            n = area[a]["n"][i]
            surface_presents += len(presents[i]) * n
            loose_space += 9 * n
        # Assume it'll be fine if you can fit 3x3 boxes in a 3k x 3t area
        # or if the used space of presents is less than 74% of the whole surface
        if loose_space < loose_surface or surface_presents < 0.74 * area[a]["s"]:
            ok += 1
        # if not, actually check
        elif surface_presents < area[a]["s"]:
            if solve(presents, area[a]) > 0:
                ok += 1

    print("Partie 1:", ok)
