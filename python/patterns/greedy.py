
def jump_game(nums):
    target, jump_start = len(nums) - 1, len(nums) - 2
    while jump_start >= 0:
        if nums[jump_start] >= target - jump_start:
            target = jump_start
        jump_start -= 1
    return target == 0

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
