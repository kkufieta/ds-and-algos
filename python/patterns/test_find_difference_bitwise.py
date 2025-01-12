import pytest
from find_difference_bitwise import *

@pytest.mark.parametrize("str1, str2, index", [
    ("wxyz", "zwxgy", 3),
    ("cbda", "abc", 2),
    ("aaaaa", "aaaaaa", 0),
    ("courae", "couearg", 6),
    ("hello", "helo", 2),
    ("mpon", "mno", 1),
    ("wxyz", "wxytz", 3),
    ("hello", "nhello", 0),
    ("aaaaa", "aaaaaa", 0),
    ("", "g", 0),
    ("pqr", "psqr", 1),
    ("masthematic", "mathematic", 2),
    ("rest", "est", 0),
    ("", "", -1),
    ("mein Name ist", "mein Name ist", -1)
])

def test_find_difference(str1, str2, index):
    assert find_difference(str1, str2) == index