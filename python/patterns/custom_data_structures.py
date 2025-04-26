import copy
'''
“SnapshotArray”: Constructor
“set”: Set Value (idx, val)
“snap”: Snapshot()
“get” : Get Value (idx, Snap ID)
'''

class SnapshotArray:

    def __init__(self, length):
        self.length = length
        self.snap_id = -1
        self.snap_map = {}
        self.current_id = 0
        self.snaps = {0: {}}
        self.new_changes = False

    def _internal_state(self):
        a = [0] * self.length
        for idx, val in self.snaps[self.current_id].items():
            a[idx] = val
        return a

    def set_value(self, idx, val):
        if (len(self.snaps[self.current_id]) == 0
            or idx not in self.snaps[self.current_id]
            or self.snaps[self.current_id][idx] != val):

            self.new_changes = True
            self.snaps[self.current_id][idx] = val

    def get_value(self, idx, snap_id):
        if self.snap_id < 0 or snap_id < 0 or snap_id > self.snap_id or idx < 0 or idx >= self.length:
            return -1

        snap = lambda snap_id: self.snaps[self.snap_map[snap_id]]
        return snap(snap_id)[idx] if idx in snap(snap_id) else 0

    def snapshot(self):
        if self.snap_id == -1 or self.new_changes:
            self.snaps[self.current_id + 1] = copy.deepcopy(self.snaps[self.current_id])
            self.current_id += 1
        self.new_changes = False
        self.snap_id += 1
        self.snap_map[self.snap_id] = self.current_id - 1
        return self.snap_id