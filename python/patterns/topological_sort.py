from collections import deque, defaultdict

def compilation_order(dependencies):
    in_degree, graph = defaultdict(int), defaultdict(list)

    for child, parent in dependencies:
        if parent not in in_degree:
            in_degree[parent] = 0
        if child not in graph:
            graph[child] = []

        in_degree[child] += 1
        graph[parent].append(child)

    compilation_order = []
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    while len(queue) != 0:
        node = queue.popleft()
        compilation_order.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return compilation_order