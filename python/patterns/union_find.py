from lib import union_find

class UnionFind:
    def __init__(self, n):
        self.dsu = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]

    def union(self, a, b):
        a_rep = self.find_parent(a)
        b_rep = self.find_parent(b)
        child = a_rep if self.rank[a_rep] < self.rank[b_rep] else b_rep
        parent = a_rep if self.rank[a_rep] >= self.rank[b_rep] else b_rep

        self.dsu[child] = self.dsu[parent]
        self.rank[parent] += self.rank[child]
        self.rank[child] = 1

    def find_parent(self, v):
        root = v
        while self.dsu[root] != root:
            root = self.find_parent(self.dsu[root])
        
        self.dsu[v] = root
        return root
    
    def set_parent(self, child, new_parent):
        self.dsu[child] = new_parent


def redundant_connection(edges):
    uf = union_find.UnionFind(len(edges))
    redundant_edge = []
    for a, b in edges:
        if uf.find(a) == uf.find(b):
            redundant_edge = [a, b]
        else:
            uf.union(a, b)

    return redundant_edge

# TODO[kat]: Use union find that's implemented in lib
class World:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.map = UnionFind(rows*cols + 1)
        for i in range(1, rows*cols + 1):
            self.map.union(0, i)

    def print(self):
        idx = lambda r, c: (r-1)*self.cols + c
        m = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(1, self.rows+1):
            for c in range(1, self.cols+1):
                m[r-1][c-1] = self.map.find_parent(idx(r, c))
            print(m[r-1])
        print()

    def _clean_up(self):
        idx = lambda r, c: (r-1)*self.cols + c
        for r in range(1, self.rows+1):
            for c in range(1, self.cols+1):
                self.map.find_parent(idx(r, c))


    def set_water(self, row, col):
        idx = lambda r, c: (r-1)*self.cols + c
        self.map.set_parent(idx(row, col), idx(row, col))
        for cell in self._adjacent_cells(row, col):
            if self.map.dsu[idx(*cell)] != 0:
                self.map.union(idx(*cell), idx(row, col))
        self._clean_up()

    def is_blocked(self):
        idx = lambda r, c: (r-1)*self.cols + c
        left_side = set()
        for r in range(1, self.rows+1):
            left_side.add(self.map.dsu[idx(r, 1)])
        for r in range(1, self.rows+1):
            right_side_cell = self.map.dsu[idx(r, self.cols)]
            if right_side_cell != 0 and right_side_cell in left_side:
                return True
        return False

    def _adjacent_cells(self, row, col):
        adjacent_cells = []
        for c in [col-1, col, col+1]:
            if c >= 1 and c <= self.cols:
                for r in [row-1, row, row+1]:
                    if r >= 1 and r <= self.rows and not (r == row and c == col):
                        adjacent_cells.append((r, c))
        return adjacent_cells



def last_day_to_cross(rows, cols, water_cells):
    w = World(rows, cols)
    
    for last_day, cell in enumerate(water_cells):
        w.set_water(*cell)
        if w.is_blocked():
            return last_day

    return -1
