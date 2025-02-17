import pytest
from lib import tree


@pytest.mark.parametrize("bt_list", [
    [],
    [1],
    [9, 8],
    [1, 2, 3, 4, 5, 6],
    [12, 7, 1, 9, 10, 15],
    [3, 9, 20, 15, 7],
    [1, 2],
    [9, 7, None, None, 1, 8, 10, None, 12],
    [1, 2, 3, None, None, 4, 5, 6],
    [3, 9, 20, None, None, 15, 7],
    [3, None, 20, None, 7],
    [5, 6, 7, None, None, 8, 9],
    [5, None, 6, None, 7, None, 8, None, 9],
    [4, 10, 20, None, None, 15, 7],
    [1, 2, 3, 4, 5, None, None, 8, None, 9, None, 10, None, 11],
])

def test_tree_list_funcs(bt_list):
    bt = tree.BinaryTree()
    bt.create_from_list(bt_list)
    print(bt.to_list(), bt_list)
    assert bt.to_list() == bt_list

def test_tree():
    bt = tree.BinaryTree()
    assert bt.root == None
    assert bt.to_list() == []

    bt.root = tree.BinaryTreeNode(5)
    assert bt.root != None
    assert bt.root.left == None
    assert bt.root.right == None
    assert bt.root.data == 5
    assert bt.to_list() == [5]

    bt.root.left = tree.BinaryTreeNode('a')
    left_node = bt.root.left
    assert bt.root != None
    assert bt.root.left != None
    assert bt.root.right == None
    assert bt.root.data == 5
    assert left_node.data == 'a'
    assert left_node.left == None
    assert left_node.right == None
    assert bt.to_list() == [5, 'a']
