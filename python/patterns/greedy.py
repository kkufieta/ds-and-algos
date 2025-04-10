
def jump_game(nums):
    if len(nums) == 0:
        return False
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

def jump_game_backtracking(nums):
    def jump(index):
        if index == len(nums) - 1:
            return True
        if index < len(nums) - 1 and nums[index] > 0:
            for i in range(nums[index], 0, -1):
                if jump(index + i):
                    return True
            nums[index] = -1
        return False
    
    return jump(0)    
