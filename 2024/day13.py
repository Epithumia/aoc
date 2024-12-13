from parse import parse
from ortools.linear_solver import pywraplp


class Machine:
    def __init__(self, a, b, p):
        r = parse("Button A: X+{ax:d}, Y+{ay:d}", a)
        self.ax, self.ay = r["ax"], r["ay"]
        r = parse("Button B: X+{bx:d}, Y+{by:d}", b)
        self.bx, self.by = r["bx"], r["by"]
        r = parse("Prize: X={x:d}, Y={y:d}", p)
        self.x, self.y = r["x"], r["y"]

    def play(self, long=False):
        solver = pywraplp.Solver.CreateSolver("SCIP")
        infinity = solver.infinity()
        a = solver.IntVar(0, infinity, "a")
        b = solver.IntVar(0, infinity, "b")
        solver.Add(a * self.ax + b * self.bx == self.x + (10000000000000 * long))
        solver.Add(a * self.ay + b * self.by == self.y + (10000000000000 * long))
        if not long:
            solver.Add(a <= 100)
            solver.Add(b <= 100)
        solver.Minimize(3 * a + b)
        status = solver.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            return solver.Objective().Value(), a.solution_value(), b.solution_value()
        else:
            return 0, 0, 0


machines = []

with open("2024/input/day13") as f:
    data = f.read().splitlines()

    nb_machines = (len(data) + 1) // 4

    for i in range(nb_machines):
        machines.append(Machine(data[4 * i], data[4 * i + 1], data[4 * i + 2]))


print("Part 1:", sum([int(m.play()[0]) for m in machines]))
print("Part 2:", sum([int(m.play(long=True)[0]) for m in machines]))