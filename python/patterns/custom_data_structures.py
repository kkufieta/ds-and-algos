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

    def _internal_state(self):
        a = [0] * self.length
        for idx, val in self.current:
            a[idx] = val
        return a

    def set_value(self, idx, val):
        pass

    def get_value(self, idx, snap_id):
        return -1

    def snapshot(self):
        return -1