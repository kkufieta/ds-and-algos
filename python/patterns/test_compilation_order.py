import pytest
from compilation_order import compilation_order


@pytest.mark.parametrize("dependencies, expected", [
    ([["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]], ["A","B","C","D","E"]),
    ([["B","A"],["C","A"],["D","B"],["E","B"],["E","D"],["E","C"],["F","D"],["F","E"],["F","C"]], ["A","B","C","D","E","F"]),
    ([["A","B"],["B","A"]], []),
    ([["B","C"],["C","A"],["A","F"]], ["F","A","C","B"]),
    ([["C","C"]], []),
])
def test_compilation_order(dependencies, expected):
    assert compilation_order(dependencies) == expected