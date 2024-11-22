def countDP(dist):
    dp = [0 for i in range(dist+1)]
    dp[0] = 1
    if dist >= 1:
        dp[1] = 1
    if dist >= 2:
        dp[2] = 2
    for i in range(3, dist+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[dist]

if __name__ == "__main__":
    dist = 4
    print(countDP(dist))