from functools import reduce

with open("2025/input/day06") as f:
    data = f.read().splitlines()

    problems = []
    ops = []

    for row in data:
        num = []
        if "+" in row or "*" in row:
            for x in row.split(" "):
                if x != "":
                    ops.append(x)
        else:
            for x in row.split(" "):
                if x != "":
                    num.append(int(x))
            problems.append(num)

partie1 = 0

for i in range(len(ops)):
    if ops[i] == "+":
        partie1 += sum(problems[k][i] for k in range(len(problems)))
    else:
        partie1 += reduce(
            lambda x, y: x * y, [problems[k][i] for k in range(len(problems))]
        )

print("Partie 1:", partie1)

cols = max(len(row) for row in data)
rows = len(data)

vals = []
partie2 = 0
op = ""
flag = False
for c in range(cols):
    if op == "":
        op = data[rows - 1][c]
    n = ""
    for r in range(rows - 1):
        n += data[r][c]
    try:
        x = int(n)
        vals.append(x)
    except:
        flag = True
    if c == cols - 1 or flag:
        if op == "+":
            partie2 += sum(vals)
        else:
            partie2 += reduce(lambda x, y: x * y, vals)
        vals = []
        op = ""
        flag = False


print("Partie 2:", partie2)
