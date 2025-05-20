def knapsack_0_1(capacity, weights, values):
    vals = [0] * (capacity + 1)

    for w, v in zip(weights[:-1], values[:-1]):
        for c in range(capacity, w-1, -1):
            vals[c] = max(vals[c], v + vals[c-w])

    return max(vals[-1], values[-1] + vals[-1 - weights[-1]])


def fibonacci_recursive_naive(num):
    if num <= 1:
        return num
    else:
        return fibonacci_recursive_naive(num-1) + fibonacci_recursive_naive(num-2)

def fibonacci_sequential(num):
    if num <= 1:
        return num
    i, n1, n2 = 2, 0, 1
    for i in range(1, num):
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
    return n2