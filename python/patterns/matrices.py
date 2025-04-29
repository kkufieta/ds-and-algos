def set_zeroes(mat):
    if len(mat) == 0 or len(mat[0]) == 0:
        return mat
    num_rows = len(mat)
    num_cols = len(mat[0])

    is_zero = lambda el: el == 0
    first_row = any(map(is_zero, mat[0]))
    first_col = any(map(is_zero, [row[0] for row in mat]))

    for row in range(1, num_rows):
        for col in range(1, num_cols):
            if mat[row][col] == 0:
                mat[0][col] = 0
                mat[row][0] = 0

    for col in range(1, num_cols):
        if mat[0][col] == 0:
            for row in range(1, num_rows):
                mat[row][col] = 0
        elif first_row:
            mat[0][col] = 0

    for row in range(1, num_rows):
        if mat[row][0] == 0:
            for col in range(1, num_cols):
                mat[row][col] = 0
        elif first_col:
            mat[row][0] = 0
    
    if first_row or first_col:
        mat[0][0] = 0

    return mat

def print_mat(mat):
    for row in mat:
        print(row)
    print()