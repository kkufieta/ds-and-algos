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
        self.current = {}
        self.snap_id = -1
        self.snaps = {}
        self.__snap_id = -1
        self.__snaps = {}
        self.new_changes = False

    def _internal_state(self):
        a = [0] * self.length
        for idx, val in self.current.items():
            a[idx] = val
        return a

    def set_value(self, idx, val):
        if len(self.current) == 0 or idx not in self.current or self.current[idx] != val:
            self.new_changes = True
            self.current[idx] = val

    def get_value(self, idx, snap_id):
        if self.snap_id < 0 or snap_id < 0 or snap_id > self.snap_id or idx < 0 or idx >= self.length:
            return -1

        snap = lambda snap_id: self.__snaps[self.snaps[snap_id]]
        return snap(snap_id)[idx] if idx in snap(snap_id) else 0

    def snapshot(self):
        if self.snap_id == -1 or self.new_changes:
            self.__snap_id += 1
            self.__snaps[self.__snap_id] = copy.deepcopy(self.current)
        self.new_changes = False
        self.snap_id += 1
        self.snaps[self.snap_id] = self.__snap_id
        return self.snap_id