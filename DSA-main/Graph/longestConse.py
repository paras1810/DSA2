def dfs(start, longest):
    if start not in longest:
        return 0

    if longest[start] != 0:
        return longest[start]

    current_longest = 1 + dfs(start + 1, longest)
    longest[start] = current_longest
    return current_longest

def longest_consecutive(arr):
    if len(arr) == 1:
        return 1
    max_length = 1
    longest = dict(map(lambda n: (n, 0), arr))
    for num in arr:
        max_length = max(max_length, dfs(num, longest))
    return max_length


if __name__ == "__main__":
    arr = [1, 9, 3, 10, 4, 20, 2]
    print("Length of the Longest consecutive subsequence is", longest_consecutive(arr))