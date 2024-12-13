from parse import parse


class Machine:
    def __init__(self, a, b, p):
        r = parse("Button A: X+{ax:d}, Y+{ay:d}", a)
        self.ax, self.ay = r["ax"], r["ay"]
        r = parse("Button B: X+{bx:d}, Y+{by:d}", b)
        self.bx, self.by = r["bx"], r["by"]
        r = parse("Prize: X={x:d}, Y={y:d}", p)
        self.x, self.y = r["x"], r["y"]
        self.x2, self.y2 = r["x"] + 10000000000000, r["y"] + 10000000000000


with open("2024/input/day13") as f:
    data = f.read().splitlines()
    nb_machines = (len(data) + 1) // 4
    machines = [
        Machine(data[4 * i], data[4 * i + 1], data[4 * i + 2])
        for i in range(nb_machines)
    ]

p1 = 0
p2 = 0
for m in machines:
    B = (m.ay * m.x - m.ax * m.y) / (m.ay * m.bx - m.ax * m.by)
    A = (m.x - B * m.bx) / m.ax
    B2 = (m.ay * m.x2 - m.ax * m.y2) / (m.ay * m.bx - m.ax * m.by)
    A2 = (m.x2 - B2 * m.bx) / m.ax
    if int(B) == B and int(A) == A:
        p1 += 3 * int(A) + int(B)
    if int(B2) == B2 and int(A2) == A2:
        p2 += 3 * int(A2) + int(B2)
print("Part 1:", p1)
print("Part 2:", p2)
