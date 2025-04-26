import pytest
from custom_data_structures import *


'''
Strings in action array are mapped as follows:
* snapshot_array: Constructor(length)
* set_value: Set Value (idx, val)
* snapshot: Snapshot()
* get_value : Get Value (idx, Snap ID)
'''

snapshot_array = "snapshot_array"
set_value = "set_value"
get_value = "get_value"
snapshot = "snapshot"

@pytest.mark.parametrize("actions, inputs, expected_outputs, expected_current_states", [
[[snapshot_array, set_value, snapshot, set_value, get_value, get_value] ,
 [[3],[1, 4], [], [1, 7], [1, 0], [1, 1]],
 [None, None, 0, None, 4, 7],
 [
     [0, 0, 0],
     [0, 4, 0],
     [0, 4, 0],
     [0, 7, 0],
     [0, 7, 0],
     [0, 7, 0],
  ]],
[[snapshot_array, set_value, snapshot, get_value, set_value, snapshot, get_value] ,
 [[3],[0, 4], [], [0, 0], [1, 6], [], [1, 1]],
 [None, None, 0, 4, None, 1, 6],
 [
     [0, 0, 0],
     [4, 0, 0],
     [4, 0, 0],
     [4, 0, 0],
     [4, 6, 0],
     [4, 6, 0],
     [4, 6, 0],
 ]],
[[snapshot_array,set_value, snapshot, get_value, set_value, snapshot, get_value, get_value] ,
 [[3], [0, 6], [], [0, 0], [1, 8], [], [1, 1], [0, 1]],
 [None, None, 0, 6, None, 1, 8, 0],
 [
     [0, 0, 0],
     [6, 0, 0],
     [6, 0, 0],
     [6, 0, 0],
     [6, 8, 0],
     [6, 8, 0],
     [6, 8, 0],
     [6, 8, 0],
 ]],
[[snapshot_array,snapshot],
 [[4],[]],
 [None,0], 
 [
     [0, 0, 0, 0],
     [0, 0, 0, 0],
 ]],
[[snapshot_array,set_value,snapshot,set_value,get_value,set_value,snapshot,get_value,snapshot,get_value, get_value, get_value, snapshot, get_value, get_value, get_value, get_value],
 [[3],[0,5],[],[0,6],[0,0],[0,100],[],[1,1], [], [0, 0], [0, 1], [0, 2], [], [0, 0], [0, 1], [0, 2], [0, 3]],
 [None,None,0,None,5,None,1,0, 2, 5, 6, 100, None, 0, 2, 5, 6, 100, 100], 
 [
    [0, 0, 0],
    [5, 0, 0],
    [5, 0, 0],
    [6, 0, 0],
    [6, 0, 0],
    [100, 0, 0],
    [100, 0, 0],
 ]],
[[snapshot_array,set_value,set_value,snapshot,get_value] ,
 [[2],[0,65],[1,56],[],[0,0]],
 [None,None,None,0,65], 
 [
     [0, 0],
     [65, 0],
     [65, 56],
     [65, 56],
     [65, 56],
 ]],
[[snapshot_array,set_value,set_value,snapshot,get_value],
 [[2],[0,65],[1,56],[],[1,0]],
 [None,None,None,0,56],
 [
     [0, 0],
     [65, 0],
     [65, 56],
     [65, 56],
     [65, 56],
 ]],
[[snapshot_array,set_value,set_value,snapshot,get_value],
 [[2],[0,80],[1,50],[],[1,0]],
 [None,None,None,0,50],
 [
     [0, 0],
     [80, 0],
     [80, 50],
     [80, 50],
     [80, 50],
 ]]
])
def test_snapshot_array(actions, inputs, expected_outputs, expected_current_states):
    snap_array = None
    for action, input, expected_output, expected_state in zip(actions, inputs, expected_outputs, expected_current_states):
        if action == snapshot_array:
            snap_array = SnapshotArray(input)
            assert snap_array != None
        elif action == set_value:
            assert snap_array.set_value(*input) == expected_output
        elif action == get_value:
            assert snap_array.get_value(*input) == expected_output
        elif action == snapshot:
            assert snap_array.snapshot() == expected_output
        else:
            assert False
        assert snap_array._internal_state() == expected_state
