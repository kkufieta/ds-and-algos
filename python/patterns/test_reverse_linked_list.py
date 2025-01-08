import pytest
import reverse_linked_list as rll
from lib import linked_list as ll

@pytest.mark.parametrize("nums_list", [
    [1, 2, 3, 4, 5],
    [1,-2,3,4,-5,4,3,-2,1],
    [-1,-5,-3,-7,-8,-6,-2],
    [-1,2,-3,4],
    [1,-1,-2,3,-4,5],
    [28,21,14,7],
    [0],
    [],
])

def test_reverse_linked_list(nums_list):
    linked_list = ll.LinkedList(nums_list)
    rll.reverse_linked_list(linked_list)
    assert linked_list.as_array() == nums_list[::-1]
