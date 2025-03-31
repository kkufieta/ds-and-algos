import pytest
from modified_binary_search import *

@pytest.mark.parametrize("nums, target, expected", [
    ([1,6,8,10], 1, 0),
    ([11,22,33,44,55,66,77], 33, 2),
    ([-3,-1,0,11,15], 0, 2),
    ([-30,-27,-8,-6,-1], -1, 4),
    ([0], 0, 0),
    ([], 3, -1),
    ([1,6,8,10], 2, -1),
    ([11,22,33,44,55,66,77], 32, -1),
    ([-3,-1,0,11,15], 100, -1),
    ([-30,-27,-8,-6,-1], -33, -1),
    ([0], 1, -1),
])
def test_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 4, 5, 5, 5, 5, 5, 6, 6], 5, True),
    ([10, 100, 101, 101], 101, False),
    ([1, 2, 3, 3, 3, 3, 10], 3, True),
    ([1, 1, 2, 4, 4, 4, 6, 6], 4, False),
    ([1, 1, 1, 2, 2], 1, True)
])
def test_is_majority(nums, target, expected):
    assert is_majority(nums, target) == expected