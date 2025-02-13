# Product of all other elements
def product(nums):
    if len(nums) < 2:
        return []
    
    p = [1] * len(nums)
    for i in range(1, len(nums)):
        p[-i-1] = p[-i] * nums[-i]

    num = nums[0]
    for i in range(1, len(nums)):
        p[i] *= num
        num *= nums[i]

    return p

    