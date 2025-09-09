# Note: All elements in nums are unique
def find_subsets(nums):
    subsets = [[]]

    for num in nums:
        new_subsets = []

        for subset in subsets:
            new_subsets.append(subset + [num])

        subsets.extend(new_subsets)
    
    return subsets

# Note: All elements in nums are unique
def find_subsets_using_bitmasking(nums):
    subsets = []
    for i in range(2**len(nums)):
        subset = set()
        for idx, num in enumerate(nums):
            if (i >> idx) & 1 == 1:
                subset.add(num)
        subsets.append(list(subset))
    return subsets
