import pytest
from lib import hashmap

@pytest.mark.parametrize("methods, values, expected", [
    (["DesignHashMap","put","get"] , [[],[15,250],[15]], [None,None,250]),
    (["DesignHashMap","get","get","get","remove","get"] , [[],[5],[15],[11],[11],[11]], [None,-1,-1,-1,None,-1]),
    (["DesignHashMap","get","get","put","get"] , [[],[5],[15],[15,250],[15]], [None,-1,-1,None,250]),
    (["DesignHashMap","put","put","get","remove","get"] , [[],[51,300],[15,750],[51],[51],[51]], [None,None,None,300,None,-1]),
    (["DesignHashMap","put","put","get","remove","get"] , [[],[51,300],[15,750],[51],[51],[50]], [None,None,None,300,None,-1]),
])
def test_hashmap(methods, values, expected):
    hm = None
    for i, method in enumerate(methods):
        if method == "DesignHashMap":
            hm = hashmap.HashMap()
            assert hm != expected[i]
        elif method == "put":
            key, value = values[i]
            assert hm.put(key, value) == expected[i]
        elif method == "get":
            key = values[i][0]
            assert hm.get(key) == expected[i]
        elif method == "remove":
            key = values[i][0]
            assert hm.remove(key) == expected[i]
        else:
            assert False