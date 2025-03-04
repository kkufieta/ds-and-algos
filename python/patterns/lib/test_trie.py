import pytest
from lib import trie

@pytest.mark.parametrize("methods, input, expected", [
    (["Trie","insert","search","search","search_prefix","insert","search"],
     [[],["apple"],["apple"],["app"],["app"],["app"],["app"]],
     [None,None,True,False,True,None,True]),
    (["Trie","insert","insert","insert","search_prefix","insert","search"],
     [[],["the"],["answer"],["a"],["t"],["this"],["ans"]],
     [None,None,None,None,True,None,False]),
    (["Trie","insert","search","search","search_prefix","insert","search"],
     [[],["apple"],["apple"],["app"],["app"],["app"],["app"]],
     [None,None,True,False,True,None,True]),
    (["Trie","insert","insert","search","search_prefix","insert","search_prefix"],
     [[],["hello"],["hell"],["he"],["h"],["helicopter"],["heli"]],
     [None,None,None,False,True,None,True]),
    (["Trie","insert","insert","insert","insert","search","search_prefix","search_prefix","search"],
     [[],["apple"],["banana"],["mango"],["strawberry"],["ap"],["ban"],["x"],["mango"]],
     [None,None,None,None,None,False,True,False,True]),
])
def test_trie(methods, input, expected):
    t = None
    for i, method in enumerate(methods):
        if method == "Trie":
            t = trie.Trie()
        elif method == "insert":
            assert t.insert(input[i][0]) == expected[i]
        elif method == "search":
            assert t.search(input[i][0]) == expected[i]
        elif method == "search_prefix":
            assert t.search_prefix(input[i][0]) == expected[i]
        else:
            assert False
