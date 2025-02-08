import pytest
from two_sum_problem import two_sum

@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4], 5, True),
    ([1, 2, 3, 4], 8, False),
    ([1, 2, 3, 4], 7, True),
    ([1, 2, 3, 4], 1, False),
    ([0, -1, 2, -3, 1], -2, True),
    ([0, -1, 2, -3, 1], 0, True),
    ([0, -1, 2, -3, 1], 4, False),
    ([], 5, False),
    ([5], 5, False),
    ([2, 4, 6, 8], 10, True),
    ([1, 1, 1, 1], 2, True),
    ([1, 2, 3, 4, 5], 9, True),
    ([1, 2, 3, 4, 5], 10, False),
    ([1, 2, 3, 4, 5], 3, True),
    ([1, 2, 3, 4, 5], 6, True),
    ([1, 2, 3, 4, 5], 7, True),
    ([1, 2, 3, 4, 5], 8, True),
    ([1, 2, 3, 4, 5], 11, False),
    ([1, 2, 3, 4, 5], 0, False),
    ([1, -2, 3, -4, 5], 1, True),
    ([1, -2, 3, -4, 5], -1, True),
    ([1, -2, 3, -4, 5], -3, True),
    ([1, -2, 3, -4, 5], -5, False),
    ([1, -2, 3, -4, 5], -6, True),
])

def test_two_sum(nums, k, expected):
    assert two_sum(nums, k) == expected

if __name__ == "__main__":
    pytest.main()