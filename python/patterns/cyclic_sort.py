
def find_missing_number(nums):
    i = 0
    while i < len(nums):
        n = nums[i]
        if n == 0 or n == i+1:
            i += 1
        else:
            nums[i] = nums[n-1]
            nums[n-1] = n

    for i, n in enumerate(nums):
        if n != i + 1:
            return i + 1

    return 0