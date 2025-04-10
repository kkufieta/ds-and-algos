import heapq

def number_machines(tasks):
    heapq.heapify(tasks)
    machines = []
    max_num_machines = 0
    add_task = lambda task: heapq.heappush(machines, task[1])
    while len(tasks) > 0:
        if len(machines) > 0 and machines[0] <= tasks[0][0]:
            heapq.heappop(machines)
        add_task(heapq.heappop(tasks))
        max_num_machines = max(max_num_machines, len(machines))

    return max_num_machines