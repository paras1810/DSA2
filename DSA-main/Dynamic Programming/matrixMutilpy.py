import sys
maxint = int(1e9+7)

def matrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i+l-1
            m[i][j] = maxint
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    size = len(arr)
    print(matrixChainOrder(arr, size))
