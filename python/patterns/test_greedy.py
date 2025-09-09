import pytest
from greedy import *
import time

test_cases = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([4, 2, 1, 0, 4], True),
    ([100, 2, 1, 0, 4], True), 
    ([1, 2, 3, 4, 5], True),
    ([4, 2, 3, 1, 0], True),
    ([3, 0, 0, 0, 0], False),
    ([2, 3, 1, 1, 9], True), 
    ([4, 0, 0, 0, 4], True), 
    ([0], True),
    ([1], True),
    ([], False),
]

@pytest.mark.parametrize("nums, reachable", test_cases)
def test_jump_game(nums, reachable):
    assert jump_game(nums) == reachable

@pytest.mark.parametrize("nums, reachable", test_cases)
def test_jump_game_backtracking(nums, reachable):
    assert jump_game_backtracking(nums) == reachable

def test_performance():
    global test_cases
    def run_function(func):
        for arr, _ in test_cases:
            func(arr)
    for func in [jump_game, jump_game_backtracking]:
        start = time.perf_counter()
        run_function(func)
        end = time.perf_counter()
        print(func, end - start)