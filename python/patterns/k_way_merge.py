def merge_sorted_in_place(nums1, m, nums2, n):
    p_write = m + n - 1
    m, n = m-1, n-1
    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[p_write] = nums1[m]
            m -= 1
        else:
            nums1[p_write] = nums2[n]
            n -= 1
        p_write -= 1
    
    while n >= 0:
        nums1[p_write] = nums2[n]
        n -= 1
        p_write -= 1

    return nums1