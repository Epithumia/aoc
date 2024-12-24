from collections import defaultdict, deque
import heapq
from itertools import combinations

states = defaultdict(lambda: None)
queue = deque([])


def eval_gate(in1, in2, op):
    if in1 is None or in2 is None:
        return None
    if op == "XOR":
        return in1 ^ in2
    if op == "OR":
        return in1 | in2
    if op == "AND":
        return in1 & in2


with open("2024/input/day24") as f:
    data = f.read().splitlines()

    for line in data:
        if ":" in line:
            d = line.split(": ")
            states[d[0]] = int(d[1])
        elif "->" in line:
            d = line.split(" -> ")
            output = d[1]
            inputs = d[0].split(" ")
            in1 = inputs[0]
            in2 = inputs[2]
            op = inputs[1]
            queue.append((output, in1, in2, op))

initial_states = states.copy()
initial_wires = list(queue.copy())

while len(queue) > 0:
    (output, in1, in2, op) = queue.pop()
    if (o := eval_gate(states[in1], states[in2], op)) is not None:
        states[output] = o
    else:
        queue.appendleft((output, in1, in2, op))

out_val_keys = sorted([k for k in states.keys() if k.startswith("z")], reverse=True)
out_val = int("".join([str(states[k]) for k in out_val_keys]), 2)

print("Part 1:", out_val)


def bit_diff(states):
    z_keys = sorted([k[1:] for k in states.keys() if k.startswith("z")], reverse=True)
    xy_keys = sorted([k[1:] for k in states.keys() if k.startswith("x")], reverse=True)
    if any([states[f"x{k}"] is None for k in xy_keys]):
        return 1000
    if any([states[f"y{k}"] is None for k in xy_keys]):
        return 1000
    if any([states[f"z{k}"] is None for k in z_keys]):
        return 1000
    x = int("".join(str(states[f"x{k}"]) for k in xy_keys), 2)
    y = int("".join(str(states[f"y{k}"]) for k in xy_keys), 2)
    res = x + y
    score = int.bit_length(res)
    z = int("".join(str(states[f"z{k}"]) for k in z_keys), 2)
    for i in range(score):
        if (not not (res & (1 << i))) == (not not (z & (1 << i))):
            score -= 1
        else:
            return score
    return score


def score(states, queue, swaps):
    current_state = states.copy()
    current_queue = queue.copy()
    for a, b in swaps:
        xoutput, xin1, xin2, xop = current_queue[a]
        youtput, yin1, yin2, yop = current_queue[b]
        current_queue[a] = (xoutput, yin1, yin2, yop)
        current_queue[b] = (youtput, xin1, xin2, xop)
    failure = 0
    current_queue = deque(current_queue)
    while len(current_queue) > 0 and failure < 1000:
        (output, in1, in2, op) = current_queue.pop()
        if (o := eval_gate(current_state[in1], current_state[in2], op)) is not None:
            current_state[output] = o
            failure = 0
        else:
            current_queue.appendleft((output, in1, in2, op))
            failure += 1
    if failure == 1000:
        return 1000
    return bit_diff(current_state)


def find_swaps(states, wires, initial_swaps=()):
    queue = []
    potential_wires = list(x for x in range(len(wires)))
    new_score = score(states, wires, initial_swaps)
    xy_keys = sorted([k[1:] for k in states.keys() if k.startswith("x")], reverse=True)
    new_state = states.copy()
    for k in xy_keys:
        new_state[f"x{k}"] = 1
        new_state[f"y{k}"] = 1
    new_score = max(new_score, score(new_state, wires, initial_swaps))
    new_state = states.copy()
    for k in xy_keys:
        new_state[f"x{k}"] = 1 if int(k) % 2 else 0
        new_state[f"y{k}"] = 0 if int(k) % 2 else 1
    new_score = max(new_score, score(new_state, wires, initial_swaps))
    new_state = states.copy()
    for k in xy_keys:
        new_state[f"x{k}"] = 1 if int(k) % 2 else 0
        new_state[f"y{k}"] = 1 if int(k) % 2 else 0
    new_score = max(new_score, score(new_state, wires, initial_swaps))
    new_state = states.copy()
    for k in xy_keys:
        new_state[f"x{k}"] = 1
    new_state["y00"] = 1
    new_score = max(new_score, score(new_state, wires, initial_swaps))
    heapq.heappush(queue, (new_score, initial_swaps))
    while len(queue) > 0:
        (the_score, swaps) = heapq.heappop(queue)
        if the_score == 0 and len(swaps) == 4:
            return swaps
        elif the_score == 0:
            continue
        changes = [element for p in swaps for element in p]
        for a, b in combinations(potential_wires, 2):
            if a not in changes and b not in changes:
                new_swaps = swaps + ((a, b),)
                if len(new_swaps) <= 4:
                    new_score = score(states, wires, new_swaps)
                    new_state = states.copy()
                    for k in xy_keys:
                        new_state[f"x{k}"] = 1
                        new_state[f"y{k}"] = 1
                    new_score = max(new_score, score(new_state, wires, new_swaps))
                    new_state = states.copy()
                    for k in xy_keys:
                        new_state[f"x{k}"] = 1 if int(k) % 2 else 0
                        new_state[f"y{k}"] = 0 if int(k) % 2 else 1
                    new_score = max(new_score, score(new_state, wires, new_swaps))
                    new_state = states.copy()
                    for k in xy_keys:
                        new_state[f"x{k}"] = 1 if int(k) % 2 else 0
                        new_state[f"y{k}"] = 1 if int(k) % 2 else 0
                    new_score = max(new_score, score(new_state, wires, new_swaps))
                    new_state = states.copy()
                    for k in xy_keys:
                        new_state[f"x{k}"] = 1
                    new_state["y00"] = 1
                    new_score = max(new_score, score(new_state, wires, new_swaps))
                    if new_score < the_score:
                        heapq.heappush(queue, (new_score, new_swaps))


raw_solution = find_swaps(initial_states, initial_wires)

print(raw_solution)

solution = []
for pair in raw_solution:
    solution.append(initial_wires[pair[0]][0])
    solution.append(initial_wires[pair[1]][0])

print("Part 2", ",".join(sorted(solution)))
