Steps = [
        [-1,0], # Up
        [0,1],  # Right
        [1,0], # bottom
        [0,-1] # Left
    ]

def withinLimits(row_num, col_num, total_rows, total_cols):
    if 0 <= row_num <total_rows and 0 <= col_num <total_cols:
        return True
    return False


def waterSlope(oceanMatrix, matrix, row, col):
    nrow, ncols = len(matrix), len(matrix[0])
    for i in Steps:
        if withinLimits(row+i[0], col+i[1], nrow, ncols):
            if matrix[row+i[0]][col+i[1]] >= matrix[row][col] and not oceanMatrix[row+i[0]][col+i[1]]:
                oceanMatrix[row+i[0]][col+i[1]] = True
                waterSlope(oceanMatrix, matrix, row+i[0], col+i[1])


def commonWaterFlow(matrix):
    matrix_r = len(matrix)
    matrix_c = len(matrix[0])
    pacific_m = [[False for _ in range(matrix_c)] for _ in range(matrix_r)]
    atlantic_m = [[False for _ in range(matrix_c)] for _ in range(matrix_r)]

    for i in range(matrix_c):
        pacific_m[0][i] = True
        atlantic_m[matrix_r-1][i] = True

    for i in range(matrix_r):
        pacific_m[i][0] = True
        atlantic_m[i][matrix_c-1] = True

    for i in range(matrix_c):
        waterSlope(pacific_m, matrix, 0, i)
        waterSlope(atlantic_m, matrix, matrix_r-1, i)

    for i in range(matrix_r):
        waterSlope(pacific_m, matrix, i, 0)
        waterSlope(atlantic_m, matrix, i, matrix_c-1)

    count = 0
    for i in range(matrix_r):
        for j in range(matrix_c):
            if pacific_m[i][j] and atlantic_m[i][j]:
                count += 1

    return count




if __name__ == "__main__":
    mat = [[1, 2, 2, 3, 5],  # T-T-T-T-T     F-F-F-F-T
           [3, 2, 3, 4, 4],  # T-T-T-T-T     F-F-F-T-T
           [2, 4, 5, 3, 1],  # T-T-T-F-F     F-F-T-T-T
           [6, 7, 1, 4, 5],  # T-T-F-F-F     T-T-T-T-T
           [5, 1, 1, 2, 4]]  # T-F-F-F-F     T-T-T-T-T
    print(commonWaterFlow(mat))