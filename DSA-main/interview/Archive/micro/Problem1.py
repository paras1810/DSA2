# Given an integer n, return the least number of perfect square numbers that sum to n.
#
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with
# itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
def countLeast(n, lst):
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for num in lst:
            if i - num >= 0:
                dp[i] = min(dp[i], dp[i-num]+1)
    return dp[n]

def countLeastRecur(n, lst):
    if n == 0:
        return 0
    result = float('inf')
    for num in lst:
        if num <= n:
            sub_res = countLeastRecur(n-num, lst)
            result = min(result, sub_res+1)
    return result

def allSquares(n):
    print(n)
    lst = []
    for i in range(1, n+1):
        if i*i <= n:
            lst.append(i*i)
        else:
            break
    return lst

if __name__ == "__main__":
    n = 12
    lst = allSquares(n)
    print(lst)
    print(countLeast(n, lst))
    print(countLeastRecur(n, lst))
# Example 1:
# Input: n = 12
# Output: 3, Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
# Input: n = 13
# Output: 2, Explanation: 13 = 4 + 9