import pytest
from fast_and_slow_pointer import *

@pytest.mark.parametrize("num, expected", [
    (23, True),
    (2, False),
    (1, True),
    (28, True),
    (4, False),
    (19, True),  # 19 is a happy number
    (7, True),   # 7 is a happy number
    (20, False), # 20 is not a happy number
    (100, True), # 100 is a happy number
    (85, False), # 85 is not a happy number
    (10, True),  # 10 is a happy number
    (3, False),  # 3 is not a happy number
])
def test_happy_number(num, expected):
    assert happy_number(num) == expected

@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3, 4, 0], True),  # Cycle exists: 0 -> 1 -> 2 -> 3 -> 4 -> 0
    ([1, 2, 3, 4, 5], False), # No cycle
    ([2, 0, 1], True),        # Cycle exists: 0 -> 2 -> 1 -> 0
    ([1, 1], True),           # Cycle exists: 0 -> 1 -> 1
    ([0], True),              # Single element pointing to itself
    ([1, 2, 3, 4, 5, 0], True), # Cycle exists: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0
    ([1, 2, 3, 4, 5, 6], False), # No cycle
    ([3, 1, 2, 0], True),     # Cycle exists: 0 -> 3 -> 0
    ([2, 2, 2, 2], True),     # Cycle exists: 0 -> 2 -> 2 -> 2
    ([1, 3, 0, 4, 2], True),  # Cycle exists: 0 -> 1 -> 3 -> 4 -> 2 -> 0
])
def test_detect_cycle_in_array(arr, expected):
    assert detect_cycle(arr) == expected