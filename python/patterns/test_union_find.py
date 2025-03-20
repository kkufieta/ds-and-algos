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


@pytest.mark.parametrize("rows, cols, water_cells, last_day", [
    (2 , 2 , [[1,1],[1,2],[2,1],[2,2]], 1),
    (2 , 2 , [[1,1],[2,1],[1,2],[2,2]], 2),
    (5 , 5 , [[1,1],[2,1],[3,1],[4,1],[5,1],[1,2],[2,2],[3,2],[4,2],[5,2],[1,3],[2,3],[3,3],[4,3],[5,3],[1,4],[2,4],[3,4],[4,4],[5,4],[1,5],[2,5],[3,5],[4,5],[5,5]], 20),
    (3 , 3 , [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]], 3),
    (3 , 4 , [[2,4],[1,3],[3,3],[2,1],[2,3],[2,2],[1,4],[3,1],[1,1],[1,2],[3,2],[3,4]], 5),
])
def test_last_day_to_cross(rows, cols, water_cells, last_day):
    assert last_day_to_cross(rows, cols, water_cells) == last_day