import pytest
from word_search import find_strings

@pytest.mark.parametrize("grid, words, expected", [
    ([["C","S","L","I","M"],["O","I","L","M","O"],["O","L","I","E","O"],["R","T","A","S","N"],["S","I","T","A","C"]],
     ["SLIME","SAILOR","MATCH","COCOON"],
     ["SLIME","SAILOR"]),
    ([["C","S","L","I","M"],["O","I","B","M","O"],["O","L","U","E","O"],["N","L","Y","S","N"],["S","I","N","E","C"]],
     ["BUY","STUFF","ONLINE","NOW"],
     ["BUY","ONLINE"]),
    ([["C","O","L","I","M"],["I","N","L","M","O"],["A","L","I","E","O"],["R","T","A","S","N"],["S","I","T","A","C"]],
     ["REINDEER","IN","RAIN"],
     ["IN","RAIN"]),
    ([["P","S","L","A","M"],["O","P","U","R","O"],["O","L","I","E","O"],["R","T","A","S","N"],["S","I","T","A","C"]],
     ["TOURISM","DESTINED","POPULAR"],
     ["POPULAR"]),
    ([["O","A","A","N"],["E","T","A","E"],["I","H","K","R"],["I","F","L","V"]],
     ["OATH","PEA","EAT","RAIN"],
     ["OATH","EAT"]),
    ([[]],
     ["HI"],
     []),
    ([["O","A","A","N"],["E","T","A","E"],["I","H","K","R"],["I","F","L","V"]],
     [],
     []),
    ([["O","A","A","C"],["E","T","A","E"],["I","H","K","S"],["I","Z","L","D"]],
     ["OATH","PEA","EAT","RAIN"],
     ["OATH","EAT"]),
    ([["S", "A", "A", "T"], ["V", "E", "A", "R"], ["B", "O", "K", "S"], ["I", "L", "L", "D"]],
     ["OK", "TRAIN", "ILL", "V"],
     ["OK", "ILL", "V"]),
    ([["S',", "A", "V", "T", "Q"], ["V", "L", "A", "R", "Z"], ["B',", "I", "K", "S", "Y"], ["I',", "B", "C", "F", "X"], ["W", "I", "N", "D", "X"]],
     ["ALI", "WIND", "BIND"],
     ["ALI", "WIND", "BIND"])
])
def test_find_strings(grid, words, expected):
    assert sorted(find_strings(grid, words)) == sorted(expected)