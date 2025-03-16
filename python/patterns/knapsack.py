def knapsack_0_1(capacity, weights, values):
    vals = [0] * (capacity + 1)

    for w, v in zip(weights, values):
        for c in range(capacity, w-1, -1):
            vals[c] = max(vals[c], v + vals[c-w])

    return vals[-1]