def binary_search(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# First and last position of an element in a sorted array
def first_and_last(nums, target):
    get_mid = lambda l, r: l + (r - l)//2

    def find_index(l, r, found_func, adjust_r_func):
        while l <= r:
            mid = get_mid(l, r)
            if found_func(mid):
                return mid
            elif adjust_r_func(mid):
                r = mid - 1
            else:
                l = mid + 1
        return None

    first, last = None, None
    first_found = find_index(0, len(nums) - 1,
                             lambda x: nums[x] == target,
                             lambda x: nums[x] > target)

    if first_found:
        is_leftmost = lambda index: index == 0 or (nums[index] == target and nums[index-1] < target)
        is_rightmost = lambda index: index == len(nums) - 1 or (nums[index] == target and nums[index+1] > target)
        if is_leftmost(first_found):
            first = first_found
        else:
            first = find_index(0, first_found - 1,
                               lambda x: is_leftmost(x),
                               lambda x: nums[x] == target)
        if is_rightmost(first_found):
            last = first_found
        else:
            last = find_index(first_found + 1, len(nums) - 1,
                       lambda x: is_rightmost(x),
                       lambda x: nums[x] > target)

    return first, last


# Check if a number is the majority element in a sorted array.
def is_majority(nums, target):
    if len(nums) == 0:
        return False

    mid = lambda l, r: l + (r-l)//2

    first_found, leftmost, rightmost = None, None, None
    l, r = 0, len(nums) - 1
    while l <= r:
        m = mid(l, r)
        if nums[m] == target:
            first_found = m
            break
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1


    is_leftmost = lambda index: index == 0 or (nums[index] == target and nums[index-1] < target)
    is_rightmost = lambda index: index == len(nums)-1 or (nums[index] == target and nums[index+1] > target)
    
    if first_found:
        if is_leftmost(first_found):
            leftmost = first_found
        else:
            l, r = 0, first_found - 1
            while l <= r:
                m = mid(l, r)
                if is_leftmost(m):
                    leftmost = m
                    break
                elif nums[m] == target:
                    r = m - 1
                else:
                    l = m + 1
        if is_rightmost(first_found):
            rightmost = first_found
        else:
            l, r = first_found + 1, len(nums) - 1
            while l <= r:
                m = mid(l, r)
                if is_rightmost(m):
                    rightmost = m
                    break
                elif nums[m] == target:
                    l = m + 1
                else:
                    r = m - 1
        return (rightmost - leftmost + 1) > len(nums)//2
    
    return False