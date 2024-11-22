def isSubset(num, n, t_sum):
    dp = [[False for i in range(t_sum+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, t_sum+1):
        dp[0][i] = False
    for i in range(1, n+1):
        for j in range(1, t_sum+1):
            if j < num[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= num[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-num[i-1]]
    for i in range(0, n+1):
        for j in range(0, t_sum+1):
            print(dp[i][j], end=' ')
        print()
    return dp[n][t_sum]



if __name__ == "__main__":
    num = [3, 34, 4, 12, 5, 2]
    t_sum = 9
    n = len(num)
    if isSubset(num, n, t_sum) == True:
        print("Found a subset with target sum")
    else:
        print("No Subset with given sum")