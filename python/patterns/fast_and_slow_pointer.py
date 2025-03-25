def happy_number(n):
    def sum_of_squared_digits(n):
        s = 0
        while n != 0:
            s += (n%10)**2
            n //= 10
        return s

    p_fast, p_slow = n, n
    while p_fast != 1 and p_slow != 1:
        p_slow = sum_of_squared_digits(p_slow)
        p_fast = sum_of_squared_digits(sum_of_squared_digits(p_fast))
        if p_slow == p_fast and not p_slow == 1:
            return False

    return True

def detect_cycle(nums):
    p_fast, p_slow = 0, 0
    while p_slow < len(nums) and p_fast < len(nums):
        p_slow = nums[p_slow]
        p_fast = nums[p_fast]
        if p_fast >= len(nums):
            return False
        p_fast = nums[p_fast]
        if p_slow == p_fast:
            return True

    return False