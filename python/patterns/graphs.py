def network_delay_time(times, n, k):
    if len(times) < (n-1) or k > n or k < 1:
        return -1

    graph = {}
    for source, target, delay in times:
        if source not in graph:
            graph[source] = []
        graph[source].append((source, target, delay))
        
    if k not in graph:
        return -1

    delays = [-1] * n
    delays[k-1] = 0
    stack = graph[k]
    while len(stack) > 0:
        source, target, delay = stack.pop()
        delay += delays[source-1]
        if delays[target-1] == -1 or delays[target-1] > delay:
            delays[target-1] = delay
            if target in graph:
                stack.extend(graph[target])
    
    max_delay = 0
    for delay in delays:
        if delay == -1:
            return -1
        max_delay = max(max_delay, delay)

    return max_delay