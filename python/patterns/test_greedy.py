import pytest
from greedy import *


@pytest.mark.parametrize("nums, reachable", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([1, 2, 3, 4, 5], True),
    ([4, 2, 3, 1, 0], True),
    ([3, 0, 0, 0, 0], False),
    ([2,3,1,1,9], True),
    ([3,2,1,0,4], False),
    ([4,0,0,0,4], True),
    ([0], True),
    ([1], True),
])

def test_jump_game(nums, reachable):
    assert jump_game(nums) == reachable