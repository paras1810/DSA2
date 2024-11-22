def longestUniqueSubsttr(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    maxLength = 0
    l, r = 0, 0
    visited = [False] * 256
    while r < len(s):
        if visited[ord(s[r])]:
            while visited[ord(s[r])]:
                visited[ord(s[l])] = False
                l += 1
        visited[ord(s[r])] = True
        maxLength = max(maxLength, r-l+1)
        r += 1
    return maxLength

string = "geeksforgeeks"
length = longestUniqueSubsttr(string)
print(length)