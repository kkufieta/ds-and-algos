import pytest
from lib.find_subsets import *
@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([], [[]]),
    ([1], [[], [1]]),
    ([3, 6, 9], [[], [3], [6], [9], [3, 6], [3, 9], [6, 9], [3, 6, 9]]),
    ([2, 4], [[], [2], [4], [2, 4]]),
    ([9], [[], [9]]),
    ([6, 7, 8], [[], [6], [7], [8], [6, 7], [6, 8], [7, 8], [6, 7, 8]]),
    ([10, 20], [[], [10], [20], [10, 20]]),
    ([4], [[], [4]]),
    ([5, 10, 11], [[], [5], [10], [11], [5, 10], [5, 11], [10, 11], [5, 10, 11]]),
    ([1], [[],[1]]),
    ([1,2], [[],[1],[2],[1,2]]),
    ([2,5,7], [[],[2],[5],[2,5],[7],[2,7],[5,7],[2,5,7]]),
    ([1,2,3,4], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]]),
    ([0], [[],[0]])
])
def test_find_subsets(nums, expected):
    assert sorted(find_subsets(nums)) == sorted(expected)
    
    subsets, expected_subsets = [], []
    for subset in find_subsets_using_bitmasking(nums):
        subsets.append(sorted(subset))
    for subset in expected:
        expected_subsets.append(sorted(subset))
    
    assert sorted(subsets) == sorted(expected_subsets)