from collections import deque

def flood_fill(grid, r, c, target):
    valid_r = lambda r: r >= 0 and r < len(grid)
    valid_c = lambda c: c >= 0 and c < len(grid[0])
    valid_rc = lambda r, c: valid_r(r) and valid_c(c)
    if len(grid) == 0 or not valid_rc(r, c) or grid[r][c] == target:
        return grid
    
    val = grid[r][c]
    valid_n = lambda r, c: valid_rc(r, c) and grid[r][c] == val
    neighbors = lambda r, c: [rc for rc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)] if valid_n(*rc)]
    grid[r][c] = target
    q = deque([(r, c)])
    while len(q) != 0:
        ns = neighbors(*q.popleft())
        for r, c in ns:
            grid[r][c] = target
        q.extend(ns)
    return grid
