class UnionFind:
    def __init__(self, n):
        self.dsu = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]

    def union(self, a, b):
        child = a if self.rank[a] < self.rank[b] else b
        parent = a if self.rank[a] >= self.rank[b] else b

        self.dsu[child] = self.dsu[parent]
        self.rank[parent] += self.rank[child]
        self.rank[child] = 1

    def find_parent(self, v):
        root = v
        while self.dsu[root] != root:
            root = self.dsu[root]
        
        self.dsu[v] = root
        return root

def redundant_connection(edges):
    uf = UnionFind(len(edges))
    redundant_edge = []
    for a, b in edges:
        if uf.find_parent(a) == uf.find_parent(b):
            redundant_edge = [a, b]
        else:
            uf.union(a, b)

    return redundant_edge

def last_day_to_cross(rows, cols, water_cells):
    last_day = 0
    return last_day