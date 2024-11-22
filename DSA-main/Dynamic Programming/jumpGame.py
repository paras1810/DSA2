def minNumJump(arr, n):
    dp = [0 for i in range(n)]
    if n == 0 or arr[0] == 0:
        return float('inf')
    dp[0] = 0
    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(i):
            if i <= arr[j]+j and dp[j]!=float('inf'):
                dp[i] = min(dp[i], dp[j]+1)

    return dp[n-1]


if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    size = len(arr)
    print(minNumJump(arr, size))