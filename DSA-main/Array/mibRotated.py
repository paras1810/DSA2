def minRotated(arr, low, high):
    if arr[low] <= arr[high]:
        return arr[low]
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < arr[mid-1]:
            return arr[mid]
        elif arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid-1
    return None






if __name__ == '__main__':
    arr = [5, 6, 1, 2, 3, 4]
    n = len(arr)
    print(minRotated(arr, 0, n-1))
