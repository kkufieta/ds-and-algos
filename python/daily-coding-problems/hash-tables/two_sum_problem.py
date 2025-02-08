# two_sum problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
def two_sum(nums, k):
    matches = set()
    for num in nums:
        if num in matches:
            return True
        matches.add(k - num)
    
    return False
