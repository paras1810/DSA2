INT_MAX = 32767
def eggDrop(n, k):
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = 1
        dp[i][0] = 0

    for i in range(1, k+1):
        dp[1][i] = i

    for i in range(2, n+1):
        for j in range(2, k+1):
            dp[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1+max(dp[i-1][x-1], dp[i][j-x])
                if res < dp[i][j]:
                    dp[i][j] = res

    for i in range(0, n+1):
        for j in range(0, k+1):
            print(dp[i][j], end=" ")
        print()

    return dp[n][k]



if __name__ == "__main__":
    n, k = 3, 36
    print(eggDrop(n, k))