
def jump_game(nums):
    if len(nums) <= 1:
        return True

    target_i = len(nums) - 1

    while target_i > 0:
        i = target_i - 1
        while i >= 0:
            if (target_i - i) <= nums[i]:
                target_i = i
                break
            else:
                i -= 1
        if i < 0:
            return False

    return True