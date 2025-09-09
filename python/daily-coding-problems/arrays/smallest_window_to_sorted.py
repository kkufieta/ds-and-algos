# Locate smallest window to be sorted in order to make the whole array sorted
def smallest_window_to_be_sorted(arr):
    if len(arr) <= 1:
        return 0, 0

    l, r = 0, 0
    max_seen, min_seen = arr[0], arr[-1]

    for i in range(len(arr)):
        if arr[i] < max_seen:
            r = i
        else:
            max_seen = arr[i]

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > min_seen:
            l = i
        else:
            min_seen = arr[i]

    return l, r