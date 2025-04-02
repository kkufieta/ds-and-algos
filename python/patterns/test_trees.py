import pytest
from lib import tree
import trees as mplt

@pytest.mark.parametrize("bt_list, max_path_length", [
   ([], 0),
   ([1], 0),
   ([9, 8], 1),
   ([1, 2, 3], 2),
   ([1, 2, 3, 4, 5, 6], 4),
   ([12, 7, 1, 9, 10, 15], 4),
   ([3, 9, 20, 15, 7], 3),
   ([1, 2], 1),
   ([9, 7, None, None, 1, 8, 10, None, 12], 4),
   ([1, 2, 3, None, None, 4, 5, 6], 4),
   ([3, 9, 20, None, None, 15, 7], 3),
   ([3, None, 20, None, 7], 2),
   ([5, 6, 7, None, None, 8, 9], 3),
   ([5, None, 6, None, 7, None, 8, None, 9], 4),
   ([4, 10, 20, None, None, 15, 7], 3),
   ([1, 2, 3, 4, 5, None, None, 8, None, 9, None, 10, None, 11], 6),
   ([1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, 9, None, None, None, None, 10, 11, 12, 13], 8),
])
def test_max_path_length_tree(bt_list, max_path_length):
    bt = tree.BinaryTree(bt_list)
    assert mplt.get_max_path_length_recursive(bt.root) == max_path_length
    assert mplt.get_max_path_length_sequential(bt.root) == max_path_length
    assert mplt.diameter_of_tree(bt.root) == max_path_length

@pytest.mark.parametrize("bt_list, expected", [
   ([1, 2, 2, 3, 4, 4, 3], True), 
   ([18, 21, 21, 47, 20, 21, 47], False), 
   ([25, 4, 67, 2, 3, 3, 2], False), 
   ([1, 2, 2, 3, None, None, 3], True), 
   ([1, 2, 2, None, 3, 3, None, 4, 5, 5, 4], True), 
   ([], True), 
   ([1], True), 
   ([9, 8], False), 
   ([1, 2, 3], False), 
   ([1, 2, 2], True), 
   ([1, 2, 3, 4, 5, 6], False), 
   ([12, 7, 1, 9, 10, 15], False), 
   ([3, 9, 20, 15, 7], False), 
   ([1, 1], False), 
   ([1, 2, 2, 3, 4, 4, 3], True), 
   ([18, 21, 21, 47, 20, 21, 47], False), 
   ([25, 4, 67, 2, 3, 3, 2], False), 
   ([1, 2, 2, 3, None, None, 3], True), 
   ([1, 2, 2, None, 3, None, 3], False) 
])
def test_symmetric_binary_tree(bt_list, expected):
    bt = tree.BinaryTree(bt_list)
    assert mplt.symmetric_binary_tree(bt.root) == expected