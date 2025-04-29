import heapq

def number_machines(tasks):
    tasks.sort()
    machines = []
    for start, end in tasks:
        if machines and machines[0] <= start:
            heapq.heappop(machines)
        heapq.heappush(machines, end)

    return len(machines)