import pytest
from lib.union_find import *

@pytest.mark.parametrize("n, fnc_calls, expected_return, expected_parent, expected_rank", [
    (5, 
        [(None, None),
        ("union", (0, 1)),
        ("union", (1, 2)),
        ("union", (2, 3)),
        ("union", (4, 5)),
        ("union", (3, 5)),
        ("find", 0),
        ("find", 4)],
        [None, None, None, None, None, None, 1, 1],
        [
            [0, 1, 2, 3, 4, 5],
            [1, 1, 2, 3, 4, 5],
            [1, 1, 1, 3, 4, 5],
            [1, 1, 1, 1, 4, 5],
            [1, 1, 1, 1, 5, 5],
            [1, 1, 1, 1, 5, 1],
            [1, 1, 1, 1, 5, 1],
            [1, 1, 1, 1, 1, 1],
        ],
        [
            [1, 1, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 3, 1, 1, 1, 1],
            [1, 4, 1, 1, 1, 1],
            [1, 4, 1, 1, 1, 2],
            [1, 6, 1, 1, 1, 2],
            [1, 6, 1, 1, 1, 2],
            [1, 6, 1, 1, 1, 1],
        ]
    )
])
def test_UnionFind(n, fnc_calls, expected_return, expected_parent, expected_rank):
    uf = UnionFind(n)
    for i, (fnc_call, args) in enumerate(fnc_calls):
        if fnc_call == "union":
            assert uf.union(*args) == expected_return[i]
        elif fnc_call == "find":
            assert uf.find(args) == expected_return[i]
        assert uf.parent == expected_parent[i]
        assert uf.rank == expected_rank[i] 
        
