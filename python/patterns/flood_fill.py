def flood_fill(grid, sr, sc, target):
    if len(grid) == 0 or len(grid[0]) == 0:
        return grid

    last_row = len(grid) - 1
    last_col = len(grid[0]) - 1
    if sr < 0 or sr > last_row or sc < 0 or sc > last_col:
        return grid

    if grid[sr][sc] == target:
        return grid

    return flood(grid, sr, sc, target, grid[sr][sc])

def flood(grid, sr, sc, target, match):
    last_row = len(grid) - 1
    last_col = len(grid[0]) - 1
    if sr < 0 or sr > last_row or sc < 0 or sc > last_col:
        return grid

    if grid[sr][sc] != match:
        return grid

    grid[sr][sc] = target

    for i, j in [(sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)]:
        grid = flood(grid, i, j, target, match)

    return grid