import pytest
from lib import trie

@pytest.mark.parametrize("methods, inputs, expected", [
    (["Trie", "insert", "insert", "insert", "insert", "search", "search", "search_prefix"],
     [None, "bat", "bye", "ok", "cry", "bye", "con", "ba"],
     [None,None,None,None,None,True,False,True]),
    (["Trie", "insert", "insert", "insert", "insert", "insert", "search", "search"],
     [None, "bat", "bag", "make", "broom", "bait", "bait", "bagg"],
     [None, None, None, None, None, None, True, False]),
    (["Trie", "insert", "insert", "insert", "insert", "search_prefix", "search_prefix"],
     [None, "broke", "what", "home", "broom", "b", "x"],
     [None, None, None, None, None, True, False]),
    (["Trie","insert","search","search","search_prefix","insert","search"],
     [None,"apple","apple","app","app","app","app"],
     [None,None,True,False,True,None,True]),
    (["Trie","insert","insert","insert","search_prefix","insert","search"],
     [None,"the","answer","a","t","this","ans"],
     [None,None,None,None,True,None,False]),
    (["Trie","insert","search","search","search_prefix","insert","search"],
     [None,"apple","apple","app","app","app","app"],
     [None,None,True,False,True,None,True]),
    (["Trie","insert","insert","search","search_prefix","insert","search_prefix"],
     [None,"hello","hell","he","h","helicopter","heli"],
     [None,None,None,False,True,None,True]),
    (["Trie","insert","insert","insert","insert","search","search_prefix","search_prefix","search"],
     [None,"apple","banana","mango","strawberry","ap","ban","x","mango"],
     [None,None,None,None,None,False,True,False,True]),
])
def test_trie(methods, inputs, expected):
    t = None
    for method, input, expect in zip(methods, inputs, expected):
        if method == "Trie":
            t = trie.Trie()
            assert t != None
        elif method == "insert":
            assert t.insert(input) == expect
        elif method == "search":
            assert t.search(input) == expect
        elif method == "search_prefix":
            assert t.search_prefix(input) == expect
        else:
            assert False
