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