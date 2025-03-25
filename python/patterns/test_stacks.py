import pytest
from stacks import *

@pytest.mark.parametrize("s, expected", [
    ("sss", "s"),
    ("abbaaca", "aca"),
    ("sadkkdassa", "sa"),
    ("azxxzy", "ay"),
    ("abcde", "abcde"),
    ("aabbccdd", ""),
    ("", ""),  # Empty string
    ("a", "a"),  # Single character
    ("aa", ""),  # Two identical characters
    ("abccba", ""),  # Entire string collapses
    ("abccbaa", "a"),  # Partial collapse
    ("aabccba", "a"),  # Mixed collapse
    ("aabbccddeeff", ""),  # All pairs collapse
    ("abcdefggfedcba", ""),  # Palindrome with duplicates
    ("aabbccddeeffgghhii", ""),  # Long string with all pairs
    ("aabbccddeeffgghhiijj", ""),  # Long string with all pairs and extra
])
def test_remove_adjacent_duplicates(s, expected):
    assert remove_adjacent_duplicates(s) == expected