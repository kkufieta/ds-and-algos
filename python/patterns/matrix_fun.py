def set_zeroes(mat):
    rows = len(mat)
    if rows == 0:
        return mat
    cols = len(mat[0])

    zero_rows, zero_cols = set(), set()
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    for row in range(rows):
        for col in range(cols):
            if row in zero_rows or col in zero_cols:
                mat[row][col] = 0

    return mat
