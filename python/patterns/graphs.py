import heapq

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

def network_delay_time_optimized(times, n, k):
    if len(times) < (n-1) or k < 1 or k > n:
        return -1
    graph = {source: [] for source in range(1, n+1)}
    for source, target, time in times:
        graph[source].append((time, target))
    
    max_time = 0
    visited = set([k])
    pqueue = graph[k]
    heapq.heapify(pqueue)
    while len(pqueue) > 0:
        time, target = heapq.heappop(pqueue)
        if target not in visited:
            visited.add(target)
            max_time = max(max_time, time)
            for new_time, new_target in graph[target]:
                heapq.heappush(pqueue, (new_time + time, new_target))
    
    return -1 if len(visited) < n else max_time
