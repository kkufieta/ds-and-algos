import pytest
from topological_sort import *

A, B, C, D, E, F, G, H, I, J, K, L, M = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"
N, O, P, Q, R, S, T, U, V, W, X, Y, Z = "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" 
@pytest.mark.parametrize("dependencies, expected", [
    ([[B, A], [C, A], [D, C], [E, D], [E, B]], [[A, B, C, D, E]]), 
    ([[B, A], [C, A], [D, B], [E, B], [E, D], [E, C], [F, D], [F, E], [F, C]], [[A, B, C, D, E, F]]), 
    ([[A, B], [B, A]], [[]]), 
    ([[B, C], [C, A], [A, F]], [[F, A, C, B]]), 
    ([[C, C]], [[]]), 
    ([[C, A], [B, A], [B, C], [D, C], [D, B], [E, B], [E, D]], [[A, C, B, D, E]]), 
    ([[C, A], [B, A], [D, C], [E, B], [E, D]], [[A, B, C, D, E], [A, C, B, D, E], [A, C, D, B, E]]), 
    ([[A, B], [B, C], [A, D]], [[C, B, D, A], [D, C, B, A], [C, D, B, A]]), 
    ([[A, B], [B, C], [C, D]], [[D, C, B, A]]), 
    ([[W, X], [X, Z], [Z, Y], [Y, X]], [[]]), 
    ([[B, A], [C, A], [D, C], [E, D], [E, B]], [[A, B, C, D, E]]), 
    ([[B, A], [C, A], [D, B], [E, B], [E, D], [E, C], [F, D], [F, E], [F, C]], [[A, B, C, D, E, F]]), 
    ([[A, B], [B, A]], [[]]), 
    ([[B, C], [C, A], [A, F]], [[F, A, C, B]]), 
    ([[C, C]], [[]]), 
    ([[V, J], [E, D], [B, S], [U, L], [G, V], [D, Z], [S, L], [X, T], [F, C], [R, D], [U, R], [B, L], 
      [B, U], [U, C], [U, G], [H, J], [S, P], [J, H], [J, G], [K, B], [F, I], [V, M], [B, M], [V, H], 
      [O, M], [O, V], [G, L], [L, M], [W, J], [Q, O], [W, F], [M, V], [W, D], [C, R], [Y, R], [V, I], 
      [Q, F], [B, A], [M, Q], [C, K], [M, B], [Q, U], [J, A], [P, E], [L, U], [D, O], [C, J], [L, C], 
      [S, X], [I, C], [D, T], [P, I], [N, O], [O, W], [D, B], [Q, A], [G, S], [B, F], [K, N], [U, F], 
      [R, U], [K, Z], [M, R], [B, O], [A, Q], [S, H], [J, U], [D, E], [N, Q], [D, U], [P, B], [C, M], 
      [T, D], [A, G], [K, G], [S, E], [X, A], [B, W], [J, E], [O, A], [H, I], [U, Y], [F, B], [S, C], 
      [L, D]], [[]])
])
def test_compilation_order(dependencies, expected):
    assert compilation_order(dependencies) in expected

@pytest.mark.parametrize("words, expected_free, expected_ordered", [
    ([], {}, []),
    (["ca", "aa", "ab"], {'c'}, ['a', 'b']),
    (["ac", "ab", "zc", "zb"], {'a', 'c'}, ['z', 'b']), # 2nd is an imperfect test, since b and z are allowed to arrive in any order
    (["baa", "abcd", "abca", "cab", "cad"], {'b'}, ['d', 'a', 'c']),
    (["mdx", "mars", "avgd", "dkae"] , {}, []),
    (["m", "a", "b", "s"], {'m'}, ['a', 'b', 's']),
    (["wrt", "wrf", "er", "ett", "rftt"], {'w'}, ['e', 'r', 't', 'f']),
    (["alpha", "bravo", "charlie", "delta"] , {'l', 't', 'o', 'p', 'h', 'a', 'v', 'i', 'e', 'r'}, ['b', 'c', 'd']),
    (["jupyter", "ascending"] , {'d', 's', 't', 'y', 'p', 'e', 'i', 'g', 'n', 'u', 'r', 'j', 'c'}, ['a']),
    (["vanilla", "alpine", "algor", "port", "norm", "nylon", "ophellia", "hidden"],
     {'l', 'd', 't', 'i', 'e', 'v', 'm', 'r'}, ['a', 'p', 'g', 'n', 'o', 'y', 'h']),
    (["xro","xma","per","prt","oxh","olv"] , {'x', 't', 'e', 'h', 'a', 'v'}, ['r', 'p', 'l', 'm', 'o']),
    (["o","l","m","s"] , {'o'}, ['l', 'm', 's']),
    (["mdx","mars","avgd","dkae"], {}, []),
    (["mdxok","mrolw","mroqs","kptz","klr","klon","zvef","zrsu","zzs","orm","oqt"],
     {'s', 'x', 'w', 'n', 'p', 'u', 'm', 'f', 'd', 'v', 'e', 't'}, ['k', 'l', 'r', 'z', 'q', 'o']),
    (["m","mx","mxe","mxer","mxerl","mxerlo","mxerlos","mxerlost","mxerlostr","mxerlostrpq","mxerlostrp"] , {}, []),
    (["xsfrwaysdqfunrimrrwk"], {'y', 'n', 'x', 'q', 'm', 'r', 'a', 's', 'd', 'u', 'i', 'f', 'k', 'w'}, [])
])
def test_alien_order(words, expected_free, expected_ordered):
    # Note: expected_free is expected to be sorted in descending order before the order of expected_ordered
    # is determined within alien_order. This is for the sake of the test to work.
    res = alien_order(words)
    i = 0
    for ch in res:
        if ch in expected_free:
            expected_free.remove(ch)
        elif len(expected_ordered) > 0:
            assert i < len(expected_ordered)
            assert ch == expected_ordered[i]
            i += 1
    assert len(expected_free) == 0
    assert i == len(expected_ordered)
