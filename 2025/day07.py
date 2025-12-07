with open("2025/input/day07") as f:
    data = f.read().splitlines()

    diagram = [list(row) for row in data]
    potential = [[0 for _ in range(len(diagram[0]))] for _ in range(len(diagram))]

    for j in range(len(diagram[0])):
        if diagram[0][j] == "S":
            diagram[1][j] = "|"
            potential[1][j] = 1
    for i in range(1, len(diagram) - 1):
        for j in range(len(diagram[i])):
            if diagram[i][j] == "^":
                diagram[i][j - 1] = "|"
                potential[i][j - 1] += potential[i - 1][j]
                diagram[i][j + 1] = "|"
                potential[i][j + 1] += potential[i - 1][j]
        for j in range(len(diagram[i])):
            if diagram[i][j] == "|" and diagram[i + 1][j] == ".":
                diagram[i + 1][j] = "|"
                potential[i + 1][j] += potential[i][j]

    partie1 = 0

    for i in range(len(diagram) - 1):
        for j in range(len(diagram[i])):
            if diagram[i + 1][j] == "^" and diagram[i][j] == "|":
                partie1 += 1

    print("Partie 1:", partie1)

    partie2 = sum(x for x in potential[-1])

    print("Partie 2:", partie2)
