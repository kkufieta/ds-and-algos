from collections import defaultdict

def compilation_order(dependencies):
    in_degree, graph = defaultdict(int), defaultdict(list)

    for child, parent in dependencies:
        if parent not in in_degree:
            in_degree[parent] = 0
        if child not in graph:
            graph[child] = []

        in_degree[child] += 1
        graph[parent].append(child)

    i, compilation_order = 0, [node for node in in_degree if in_degree[node] == 0]
    while i < len(compilation_order):
        for child in graph[compilation_order[i]]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                compilation_order.append(child)
        i += 1

    return compilation_order