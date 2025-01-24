import heapq

def number_machines(tasks):
    if len(tasks) <= 1:
        return len(tasks)

    heapq.heapify(tasks)

    machines = []
    while len(tasks) > 0:
        t = heapq.heappop(tasks)

        if len(machines) == 0 or t[0] < machines[0]:
            heapq.heappush(machines, t[1])
        else:
            heapq.heapreplace(machines, t[1])

    return len(machines)