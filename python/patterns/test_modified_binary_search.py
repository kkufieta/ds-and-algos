import pytest
import modified_binary_search

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
    assert modified_binary_search.binary_search(nums, target) == expected