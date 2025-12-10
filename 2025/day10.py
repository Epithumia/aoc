from math import inf
from ortools.linear_solver import pywraplp


def generate_states(n: int):
    for i in range(2**n):
        yield [int(x) for x in bin(i)[2:].zfill(n)]


class Machine:
    def __init__(self, data) -> None:
        parts = data.split(" ")
        self.target_state = [0 if x == "." else 1 for x in parts[0][1:-1]]
        self.target_joltage = [int(j) for j in parts[-1][1:-1].split(",")]
        self.buttons = [
            [int(x) for x in button[1:-1].split(",")] for button in parts[1:-1]
        ]
        self.state = [0 for _ in self.target_state]

    def press(self, button):
        for b in button:
            self.state[b] = (self.state[b] + 1) % 2

    def solve_part1(self):
        best = inf
        for state in generate_states(len(self.buttons)):
            for bit in range(len(state)):
                if state[bit] == 1:
                    self.press(self.buttons[bit])
            if self.state == self.target_state:
                best = min(best, sum(state))
            self.reset()
        return best

    def solve_part2(self):

        solver = pywraplp.Solver.CreateSolver("SAT")

        joltage_buttons = [
            solver.IntVar(0, 400, f"presses for {j}") for j in range(len(self.buttons))
        ]

        for i in range(len(self.target_joltage)):
            switches = [1 if i in button else 0 for button in self.buttons]
            solver.Add(
                sum(switches[k] * joltage_buttons[k] for k in range(len(self.buttons)))
                == self.target_joltage[i]
            )

        solver.Minimize(sum(joltage_buttons))

        solver.Solve()
        return int(solver.Objective().Value())

    def reset(self):
        self.state = [0 for _ in self.target_state]

    def __str__(self):
        return f"{self.target_state} {self.target_joltage} {self.buttons}"


with open("2025/input/day10") as f:
    data = f.read().splitlines()

    machines = [Machine(row) for row in data]

    print("Partie 1:", sum([m.solve_part1() for m in machines]))

    print("Partie 2:", sum([m.solve_part2() for m in machines]))
