import pytest
from dp_word_break import *

@pytest.mark.parametrize("s, word_dict, expected", [
    ("magiclly",
     ["ag","al","icl","mag","magic","ly","lly"],
     ["mag icl ly","magic lly"]),
    ("raincoats",
     ["rain","oats","coat","s","rains","oat","coats","c"],
     ["rain c oat s","rain c oats","rain coat s","rain coats"]),
    ("highway",
     ["crash","cream","high","highway","low","way"],
     ["high way","highway"]),
    ("robocat",
     ["rob","cat","robo","bo","b"],
     ["robo cat"]),
    ("cocomomo",
     ["co","mo","coco","momo"],
     ["co co mo mo","co co momo","coco mo mo","coco momo"]),
    ("catsanddog",
     ["cat", "and", "cats", "sand", "dog"],
     ["cats and dog", "cat sand dog"]),
     ("catsandog",
     ["cat", "and", "cats", "sand", "dog"],
     []),
     ("pineapplepenapple",
     ["apple", "pen", "applepen", "pine", "pineapple"],
     ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]),
     ("cattos",
     ["cats", "cat", "to", "os"],
     []),
     ("superdogs",
     ["super", "dogs", "dog", "s"],
     ["super dogs", "super dog s"])
])

def test_word_break(s, word_dict, expected):
    assert sorted(word_break(s, word_dict)) == sorted(expected)