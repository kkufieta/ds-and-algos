import pytest
from lib.find_subsets import find_subsets
@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([], [[]]),
    ([1], [[], [1]]),
])
def test_find_subsets(arr, expected):
    assert find_subsets(arr) == expected