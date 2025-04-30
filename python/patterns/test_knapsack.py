import pytest
from knapsack import *

@pytest.mark.parametrize("capacity, weights, values, expected", [
    (6 , [1,2,3,5] , [1,5,4,8], 10),
    (3 , [1] , [2], 2),
    (3 , [2] , [3], 3),
    (10 , [3,6,10,7,2] , [12,10,15,17,13], 30),
    (30 , [10,20,30] , [22,33,44], 55),
])

def test_knapsack_0_1(capacity, weights, values, expected):
    assert knapsack_0_1(capacity, weights, values) == expected