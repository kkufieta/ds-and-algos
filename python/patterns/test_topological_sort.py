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