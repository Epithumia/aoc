intervals = []
ids = []

with open("2025/input/day05") as f:
    data = f.read().splitlines()

    for row in data:
        if "-" in row:
            intervals.append(tuple(int(x) for x in row.split("-")))
        elif row != "":
            ids.append(int(row))


intervals.sort()

valid_id_range = []

for a, b in intervals:
    for i1, i2 in valid_id_range:
        if i1 <= a <= i2:
            if i2 < b:
                valid_id_range.remove((i1, i2))
                valid_id_range.append((i1, b))
            break
    else:
        valid_id_range.append((a, b))

partie1 = sum(any(a <= i <= b for a, b in valid_id_range) for i in ids)

print("Partie 1:", partie1)

partie2 = sum(b - a + 1 for a, b in valid_id_range)

print("Partie 2:", partie2)
