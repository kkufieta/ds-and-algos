import pytest
from intervals import *

@pytest.mark.parametrize("intervals, expected", [
    ([[1,5],[3,7],[4,6]], [[1,7]]),
    ([[1,5]], [[1, 5]]),
    ([], []),
    ([[1,5],[4,6],[6,8],[11,15]], [[1,8],[11,15]]),
    ([[1,9],[3,8],[4,4]], [[1,9]]),
    ([[1,2],[3,4],[8,8]], [[1,2],[3,4],[8,8]]),
])

def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected