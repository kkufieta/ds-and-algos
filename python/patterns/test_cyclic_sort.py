import pytest
from cyclic_sort import *

@pytest.mark.parametrize("nums, expected", [
    ([5, 6, 4, 2, 1, 3, 0, 7, 9], 8),
    ([5, 6, 10, 2, 1, 3, 0, 7, 9, 12, 11, 8], 4),
    ([0, 1, 2], 3),
    ([0, 12, 4, 6, 7, 8, 3, 9, 5, 10, 2, 1], 11),
    ([0, 2, 4, 6, 7, 8, 3, 9, 5, 10], 1),
    ([0,1,2,4], 3),
    ([3,0,1,4], 2),
    ([1,4,5,6,8,2,0,7], 3),
    ([1,0,2,3,4,5,6,8,9,7,11], 10),
    ([1], 0),
    ([], 0),
])

def test_find_missing_number(nums, expected):
    assert find_missing_number(nums) == expected