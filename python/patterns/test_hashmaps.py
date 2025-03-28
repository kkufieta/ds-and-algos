import pytest
from hashmaps import *

@pytest.mark.parametrize("s, expected", [
    ("aab", True),
    ("acb", False),
    ("abb", True),
    ("axbk", False),
    ("", True),
    ("a", True),
    ("abab", True),
    ("peas", False),
    ("racecar", True),
    ("code", False),
    ("baefeab", True),
])
def test_permutation_is_palindrome(s, expected):
    assert permutation_is_palindrome(s) == expected

@pytest.mark.parametrize("nums, expected_indices, expected_sum", [
    ([0, 1, 2, 3], [0, 3, 1, 2], 3),
    ([1, 2, 3, 4, 5, 6], [0, 5, 1, 4], 6),
    ([10, 20, 30, 40, 50, 60, 70, 80], [0, 3, 1, 2], 50),
    ([5, 5, 5, 5], [0, 1, 2, 3], 10),
    ([1, 1, 4, 7, 2, 2, 2, 2], [0, 4, 1, 5], 3),
    ([100, 200, 300, 400, 500, 600], [0, 3, 1, 2], 500),
    ([0, 0, 0, 0], [0, 1, 2, 3], 0),
    ([1, 3, 5, 7, 9, 11, 13, 15], [0, 7, 1, 6], 16),
    ([2, 4, 6, 8, 10, 12, 14, 16], [0, 6, 1, 5], 16),
    ([1, 2, 3, 4], [0, 3, 1, 2], 5),
])
def test_find_equal_sums(nums, expected_indices, expected_sum):
    assert find_equal_sums(nums) == expected_indices
    a, b, c, d = expected_indices
    assert nums[a] + nums[b] == expected_sum
    assert nums[c] + nums[d] == expected_sum