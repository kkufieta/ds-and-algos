import pytest
import random
from bitwise_fun import *

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

def test_swap_without_extra_space():
    x, y = 0, 0
    expect_y, expect_x = swap_without_extra_space(x, y)
    assert expect_x == 0
    assert expect_y == 0

    x, y = 1, 0
    expect_y, expect_x = swap_without_extra_space(x, y)
    assert expect_x == 1
    assert expect_y == 0

    for i in range(100):
        x, y = random.randint(0, 10000), random.randint(0, 10000)
        expect_y, expect_x = swap_without_extra_space(x, y)
        assert expect_x == x
        assert expect_y == y
