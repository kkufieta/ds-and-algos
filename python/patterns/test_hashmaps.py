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