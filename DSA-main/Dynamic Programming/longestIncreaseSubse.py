def lis(arr):
    n = len(arr)
    res = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and res[i]<res[j]+1:
                res[i] = res[j]+1
    return res


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))