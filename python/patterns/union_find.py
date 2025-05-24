from lib.union_find import *

def redundant_connection(edges):
    uf = UnionFind(len(edges))
    for x, y in edges:
        if uf.find(x) == uf.find(y):
            return [x, y]
        uf.union(x, y)
    return []

# Approach: Start with all cells being water, then going backwards in time
# uncover land and check if there's a connection of land from the top to the 
# bottom of the matrix at each step.
def last_day_to_cross(rows, cols, water_cells):
    land_idx = rows*cols + 2
    uf = UnionFind(land_idx, zeroes=True)
    uf.set(-1, land_idx)

    get_idx = lambda r, c: (r-1)*cols + c
    is_bottom = lambda idx: idx > (rows-1)*cols
    valid_rc = lambda r, c: r >= 1 and c >= 1 and r <= rows and c <= cols
    cardinal = lambda r, c: [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
    cardinal_idx = lambda r, c: [get_idx(*rc) for rc in cardinal(r, c) if valid_rc(*rc)]

    for d, rc in enumerate(water_cells[::-1]):
        idx = get_idx(*rc)
        uf.set(idx, idx)
        if is_bottom(idx):
            uf.union(idx, land_idx)

        for n_idx in cardinal_idx(*rc):
            if uf.get(n_idx) != 0:
                uf.union(idx, n_idx) 
        
        for top_idx in range(1, cols+1):
            if uf.get(top_idx) != 0 and uf.find(top_idx) == uf.find(land_idx):
                return rows*cols - d - 1
            
    return -1

# Approach: Check at each step if there's a connected component of
# water from the left to the right of the matrix.
def last_day_to_cross_using_edges(rows, cols, water_cells):
    n = rows * cols + 2
    left_idx, right_idx = n-1, n
    uf = UnionFind(n, zeroes=True)
    uf.set(-2, left_idx)
    uf.set(-1, right_idx)

    get_idx = lambda r, c: (r-1)*cols + c
    valid_rc = lambda r, c: r >= 1 and c >= 1 and r <= rows and c <= cols
    neighbors = lambda r, c: [(r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)] 
    valid_neighbors = lambda r, c: [get_idx(*rc) for rc in neighbors(r, c) if valid_rc(*rc)]
    left = lambda idx: idx%cols == 1
    right = lambda idx: idx%cols == 0

    for day, rc in enumerate(water_cells):
        idx = get_idx(*rc)
        uf.set(idx, idx)
        if left(idx):
            uf.union(idx, left_idx)
        elif right(idx):
            uf.union(idx, right_idx)
        else:
            uf.union(idx, idx)

        for n_idx in valid_neighbors(*rc):
            if uf.get(n_idx) != 0:
                uf.union(idx, n_idx)
        
        if uf.find(left_idx) == uf.find(right_idx):
            return day
        
    return -1