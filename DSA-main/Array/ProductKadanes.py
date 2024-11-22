def maxSubArrayProduct(arr, n):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    min_ending_here = arr[0]
    for i in range(1, n):
        temp = max(max(max_ending_here * arr[i], min_ending_here * arr[i]), arr[i])
        min_ending_here = min(min(max_ending_here * arr[i], min_ending_here * arr[i]), arr[i])
        max_ending_here = temp
        max_so_far = temp

    return max_so_far


arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(maxSubArrayProduct(arr, n))
