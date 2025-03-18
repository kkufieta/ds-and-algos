import pytest
from union_find import *

@pytest.mark.parametrize("edges, expected", [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[1,3]], [1,3]),
    ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
    ([[1,2],[1,3],[1,4],[2,3]], [2,3]),
    ([[1,2],[1,3],[1,4],[1,5],[2,5]], [2,5]),
])
def test_redundant_connection(edges, expected):
    assert redundant_connection(edges) == expected