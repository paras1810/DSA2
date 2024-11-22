
def findWays(m, n, x):
    dp = [[0]*(x+1) for i in range(n+1)]
    for j in range(1, min(m+1, x+1)):
        dp[1][j] = 1

    for i in range(2, n+1):
        for j in range(1, x+1):
            for k in range(1, min(m+1, j)):
                dp[i][j] += dp[i-1][j-k]

    return dp[-1][-1]


if __name__ == "__main__":
    print(findWays(4, 2, 1))
    print(findWays(2, 2, 3))
    print(findWays(6, 3, 8))
    print(findWays(4, 2, 5))
    print(findWays(4, 3, 5))