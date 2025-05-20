import pytest
from dynamic_programming import *

@pytest.mark.parametrize("capacity, weights, values, expected", [
    (6 , [1,2,3,5] , [1,5,4,8], 10),
    (3 , [1] , [2], 2),
    (3 , [2] , [3], 3),
    (10 , [3,6,10,7,2] , [12,10,15,17,13], 30),
    (30 , [10,20,30] , [22,33,44], 55),
])

def test_knapsack_0_1(capacity, weights, values, expected):
    assert knapsack_0_1(capacity, weights, values) == expected

fibonacci_numbers = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), 
                     (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144),
                     (13, 233), (14, 377), (15, 610), (16, 987), (17, 1597), 
                     (18, 2584), (19, 4181), (20, 6765), (21, 10946), 
                     (22, 17711), (23, 28657), (24, 46368), (25, 75025)]

@pytest.mark.parametrize("num, expected_fibonacci", fibonacci_numbers)
def test_fibonacci_recursive_naive(num, expected_fibonacci):
    assert fibonacci_recursive_naive(num) == expected_fibonacci

@pytest.mark.parametrize("num, expected_fibonacci", fibonacci_numbers)
def test_fibonacci_sequential(num, expected_fibonacci):
    assert fibonacci_sequential(num) == expected_fibonacci

@pytest.mark.parametrize("num, expected_fibonacci", fibonacci_numbers)
def test_fibonacci_dp_top_down_recursive(num, expected_fibonacci):
    assert fibonacci_dp_top_down_recursive(num) == expected_fibonacci