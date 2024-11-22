
def cutRod(prices, n):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1:
                dp[i][j] = j * prices[i-1]
            else:
                if i>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(prices[i-1] + dp[i][j-i], dp[i-1][j])

    for i in range(0, n+1):
        for j in range(0, n+1):
            print(dp[i][j], end=" ")
        print()

    return dp[n][n]

if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    n = len(prices)
    print(cutRod(prices, n))