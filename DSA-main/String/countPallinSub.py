def CountPS(str, n):
    dp = [[False for i in range(n)] for j in range(n)]
    p = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        if str[i] == str[i+1]:
            dp[i][i+1] = True
            p[i][i+1] = 1
    for gap in range(2, n):
        for i in range(n-gap):
            j = gap+i
            if str[i] == str[j] and dp[i+1][j-1]:
                dp[i][j] = True
            if dp[i][j]:
                p[i][j] = p[i][j-1] + p[i+1][j] - p[i+1][j-1] + 1
            else:
                p[i][j] = p[i][j - 1] + p[i + 1][j] - p[i + 1][j - 1]
    return p[0][n-1]


if __name__ == '__main__':
    str = "abaab"
    n = len(str)
    print(CountPS(str, n))