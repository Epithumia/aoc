from collections import deque


def count_paths(n, edges, source, destination):

    # Create adjacency list (1-based indexing)
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    topological_order = []
    while q:
        node = q.popleft()
        topological_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    ways = [0] * (n + 1)
    ways[source] = 1

    for node in topological_order:
        for neighbor in graph[node]:
            ways[neighbor] += ways[node]

    return ways[destination]


with open("2025/input/day11") as f:
    data = f.read().splitlines()

    nodes = {}

    for row in data:
        start, end = row.split(": ")
        successors = end.split(" ")
        nodes[start] = successors

    id_nodes = {}
    i = 1
    for k in nodes.keys():
        id_nodes[k] = i
        i += 1

    id_nodes["out"] = i

    graph = []
    for k, v in nodes.items():
        for e in v:
            graph.append([id_nodes[k], id_nodes[e]])

    count = count_paths(len(id_nodes), graph, id_nodes["you"], id_nodes["out"])
    print("Partie 1:", count)

    count1 = count_paths(len(id_nodes), graph, id_nodes["svr"], id_nodes["fft"])
    count2 = count_paths(len(id_nodes), graph, id_nodes["fft"], id_nodes["dac"])
    count3 = count_paths(len(id_nodes), graph, id_nodes["dac"], id_nodes["out"])
    count = count1 * count2 * count3
    print("Partie 2:", count)
