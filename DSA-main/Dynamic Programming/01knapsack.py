def knapSack(w, weight, profit, n):
    dp = [[0 for j in range(w+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif weight[i-1] <= j:
                dp[i][j] = max(profit[i-1]+dp[i-1][j-weight[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]


if __name__ == "__main__":
    profit = [120, 800, 100]
    weight = [30, 40, 20]
    w = 50
    n = len(weight)
    print(knapSack(w, weight, profit, n))

