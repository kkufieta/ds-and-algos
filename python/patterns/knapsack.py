def knapsack_0_1(capacity, weights, values):
    vals = [0] * (capacity + 1)

    for w, v in zip(weights[:-1], values[:-1]):
        for c in range(capacity, w-1, -1):
            vals[c] = max(vals[c], v + vals[c-w])

    return max(vals[-1], values[-1] + vals[-1 - weights[-1]])