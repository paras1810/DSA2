
def transpose(A):
    r, c = len(A), len(A[0])
    for i in range(0, r):
        for j in range(i+1, c):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(0, r):
        for j in range(0, c):
            print(A[i][j], end=' ')
        print()

if __name__ == '__main__':
    A = [[1, 1, 1, 1],
         [2, 2, 2, 2],
         [3, 3, 3, 3],
         [4, 4, 4, 4]]

    transpose(A)