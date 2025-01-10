import pytest
from lib import tree
import max_path_length_tree as mplt

@pytest.mark.parametrize("bt_list, max_path_length", [
   ([], 0),
   ([1], 0),
   ([9, 8], 1),
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
])

def test_max_path_length_tree(bt_list, max_path_length):
    bt = tree.BinaryTree()
    bt.create_from_list(bt_list)
    assert mplt.get_max_path_length_recursive(bt.root) == max_path_length