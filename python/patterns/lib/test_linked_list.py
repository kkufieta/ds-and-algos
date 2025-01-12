import pytest
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

class TestLinkedList:
    def test_linked_list(self, nums_list):
        linked_list = ll.LinkedList(nums_list)
        assert linked_list.as_array() == nums_list


def test_linked_list_node():
    val_1 = 5
    node_1 = ll.LinkedListNode(val_1)
    assert node_1 != None
    assert node_1.data == val_1
    assert node_1.next == None

    val_2 = -1
    node_2 = ll.LinkedListNode(val_2, node_1)
    assert node_2 != None
    assert node_2.data == val_2
    assert node_2.next == node_1



