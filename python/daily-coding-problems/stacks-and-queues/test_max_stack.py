import pytest
from max_stack import MaxStack

def test_max_stack():
    # (action, val, expected_stack, expected_max_stack, expected_max_val)
    actions = [("push", 5, [5], [5], 5), \
        ("push", 2, [5, 2], [5, 5], 5), \
        ("push", -3, [5, 2, -3], [5, 5, 5], 5), \
        ("push", 8, [5, 2, -3, 8], [5, 5, 5, 8], 8), \
        ("push", 10, [5, 2, -3, 8, 10], [5, 5, 5, 8, 10], 10), \
        ("pop", 10, [5, 2, -3, 8], [5, 5, 5, 8], 8), \
        ("push", 7, [5, 2, -3, 8, 7], [5, 5, 5, 8, 8], 8), \
        ("pop", 7, [5, 2, -3, 8], [5, 5, 5, 8], 8), \
        ("pop", 8, [5, 2, -3], [5, 5, 5], 5), \
        ("pop", -3, [5, 2], [5, 5], 5), \
        ("pop", 2, [5], [5], 5), \
        ("pop", 5, [], [], IndexError)
    ]

    max_stack = MaxStack()
    for action, val, expected_stack, expected_max_stack, expected_max_val in actions:
        if action == "push":
            max_stack.push(val)
        elif action == "pop":
            assert max_stack.pop() == val
        assert max_stack.stack == expected_stack
        assert max_stack.max_stack == expected_max_stack
        if expected_max_val != IndexError:
            assert max_stack.max() == expected_max_val

    # Test for IndexError when popping from an empty stack
    with pytest.raises(IndexError):
        max_stack.pop()

    with pytest.raises(IndexError):
        max_stack.max()

