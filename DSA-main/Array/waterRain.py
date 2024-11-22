def findWater(arr, n):
    left = [0] * n
    right = [0] * n
    water = 0
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(arr[i], left[i-1])
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(arr[i], right[i+1])

    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water





if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(findWater(arr, len(arr)))