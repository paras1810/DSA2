
def count(coins, n, target):
    dp = [[0 for j in range(target+1)]for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(target+1):
            dp[i][j] += dp[i-1][j]
            if j-coins[i-1]>=0:
                dp[i][j] += dp[i][j-coins[i-1]]
    for i in range(n+1):
        for j in range(target+1):
            print(dp[i][j], end=" ")
        print()
    return dp[n][target]

if __name__ == "__main__":
    coins = [1, 2, 3]
    n = 3
    target = 5
    print(count(coins, n, target))