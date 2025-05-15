from collections import defaultdict

def compilation_order(dependencies):
    in_degree, graph = defaultdict(int), defaultdict(list)

    for child, parent in dependencies:
        graph[parent].append(child)
        graph[child].extend([])
        in_degree[parent] += 0
        in_degree[child] += 1

    i, compilation_order = 0, [node for node in in_degree if in_degree[node] == 0]
    while i < len(compilation_order):
        for child in graph[compilation_order[i]]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                compilation_order.append(child)
        i += 1

    return compilation_order if len(compilation_order) == len(graph) else []