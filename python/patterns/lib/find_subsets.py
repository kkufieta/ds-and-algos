def find_subsets(arr):
    subsets = [[]]

    for num in arr:
        new_subsets = []

        for subset in subsets:
            new_subsets.append(subset + [num])

        subsets.extend(new_subsets)
    
    return subsets