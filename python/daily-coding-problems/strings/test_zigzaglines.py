import pytest
from zigzaglines import zigzaglines

@pytest.mark.parametrize("s, k, expected", [
    ("zigzaglines", 0, ""),
    ("zigzaglines", 1, "zigzaglines"),
    ("zigzaglines", 2, 
     "z g a l n s\n i z g i e"),
    ("zigzaglines", 3, 
     "z   a   n\n i z g i e\n  g   l   s"),
    ("zigzaglines", 4, 
     "z     l\n i   g i\n  g a   n s\n   z     e"),
    ("zigzaglines", 6, 
     "z         s\n i       e\n  g     n\n   z   i\n    a l\n     g"),
    ("short", 10, "s\n h\n  o\n   r\n    t"),
    ("longwordtest", 2, 
     "l n w r t s\n o g o d e t"),
    ("", 3, ""),
    ("a", 3, "a"),
    ("ab", 3, "a\n b"),
    ("abc", 3, "a\n b\n  c"),
])

def test_zigzaglines(s, k, expected):
    assert zigzaglines(s, k) == expected
