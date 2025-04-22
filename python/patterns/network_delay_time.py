def network_delay_time(times, n, k):
    if len(times) < (n-1):
        return -1

    t = {}
    for start, end, delay in times:
        if start in t:
            t[start].append((start, end, delay))
        else:
            t[start] = [(start, end, delay)]
        
    if k not in t:
        return -1

    delays = [-1] * n
    stack = t[k]
    while len(stack) > 0:
        start, end, delay = stack.pop()
        if end != k and (delays[end-1] == -1 or delays[end-1] > delay):
            delays[end-1] = delay
            if end in t:
                for s, e, d in t[end]:
                    if e != k:
                        stack.append((s, e, delay + d))
    
    max_delay = delays[0]
    for i, delay in enumerate(delays):
        if delay == -1  and i != (k-1):
            return -1
        max_delay = max(max_delay, delay)

    return max_delay