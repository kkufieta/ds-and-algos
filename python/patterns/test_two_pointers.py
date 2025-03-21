import pytest
from two_pointers import *

@pytest.mark.parametrize("s, expected", [
    ("aba", True),
    ("abab", False),
    ("RACEACAR", False),
    ("RACECAR", True),
    ("kaYak", True),
    ("hello", False),
    ("RaCEACAR", False),
    ("A", True),
    ("ABCDABCD", False),
])
def test_valid_palindrome(s, expected):
    assert valid_palindrome(s) == expected