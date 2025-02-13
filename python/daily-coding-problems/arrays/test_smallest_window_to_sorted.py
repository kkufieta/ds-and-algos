import pytest
from smallest_window_to_sorted import smallest_window_to_be_sorted

@pytest.mark.parametrize("arr, expected", [
    ([], (0, 0)),  # Single element
    ([1], (0, 0)),  # Single element
    ([1, 2], (0, 0)),  # Already sorted two elements
    ([2, 1], (0, 1)),  # Two elements, unsorted
    ([1, 2, 3, 4, 5], (0, 0)),  # Already sorted
    ([1, 2, 3, 3, 3, 3], (0, 0)),  # Already sorted with duplicates
    ([0, 1, 2, 3, 4, 5], (0, 0)),  # Already sorted
    ([6, 1, 2, 3, 4, 5], (0, 5)),  # First element out of order
    ([1, 2, 3, 4, 5, 0], (0, 5)),  # Last element out of order
    ([1, 3, 2, 4, 5], (1, 2)),  # Small window in the middle
    ([1, 2, 5, 3, 4], (2, 4)),  # Window towards the end
    ([1, 2, 3, 4, 3, 5], (3, 4)),  # Small window towards the end
    ([1, 3, 5, 2, 4, 6], (1, 4)),  # Larger window in the middle
    ([5, 4, 3, 2, 1], (0, 4)),  # Completely unsorted
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (0, 0)),  # Already sorted long array
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], (0, 9)),  # Completely unsorted long array
    ([1, 2, 3, 4, 5, 6, 7, 8, 10, 9], (8, 9)),  # Last two elements swapped
    ([1, 3, 2, 4, 5, 6, 7, 8, 9, 10], (1, 2)),  # Small window at the start
    ([-1, -2, -3, -4, -5], (0, 4)),  # Completely unsorted with negative numbers
    ([-5, -4, -3, -2, -1], (0, 0)),  # Already sorted with negative numbers
    ([-1, -3, -2, -4, -5], (0, 4)),  # Completely unsorted
    ([1, -1, 2, -2, 3, -3], (0, 5)),  # Alternating positive and negative numbers
    ([-1, 1, -2, 2, -3, 3], (0, 4)),  # Alternating negative and positive numbers
])

def test_smallest_window_to_be_sorted(arr, expected):
    assert smallest_window_to_be_sorted(arr) == expected
