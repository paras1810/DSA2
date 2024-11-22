def maxProfit(prices):
    n = len(prices)
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], -prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
    return max(dp[-1][0], dp[-1][1])

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    ans = maxProfit(prices)
    print(ans)