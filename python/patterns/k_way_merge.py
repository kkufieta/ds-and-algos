def merge_sorted_in_place(nums1, m, nums2, n):
    p1, p2 = m-1, n-1
    for p_write in range(m + n - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p_write] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_write] = nums2[p2]
            p2 -= 1

    return nums1