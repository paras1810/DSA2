def maxStole(hval, n):
    if n == 0:
        return 0
    if n == 1:
        return hval[0]
    if n == 2:
        return max(hval[0], hval[1])
    dp = [0] * n
    dp[0] = hval[0]
    dp[1] = max(hval[0], hval[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], hval[i]+dp[i-2])
    return dp[-1]

if __name__ == "__main__":
    hval = [6, 7, 1, 3, 8, 2, 4]
    n = len(hval)
    print(maxStole(hval, n))